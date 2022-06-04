from multiprocessing import context
from django.contrib.auth.decorators import login_required
from turtle import title
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    View,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from .models import Deduped

from django.core.files.base import ContentFile
import csv
from io import StringIO

import pickle
import recordlinkage
import pandas as pd
import json

from django.core.files.storage import default_storage

# Create your views here.
with open('model_pickle', 'rb') as f:
    nb_predictions = pickle.load(f)

def home(request):
    context = {
        'title':'Home'
        
    }
            
    return render(request, "dedupeapp/home.html", context)

@login_required()
def dedupe_results(request):

        dup_pairs = []
        num_records = created_pairs = num_predictions = 0
        deduped_set = None
        if request.method == 'POST':
            
            file = request.FILES['file']
            print('FILE RECEIVED', file)

            patientsfile = pd.read_csv(file)
            correct_headers = ['Patient_ID', 'Name', 'Address', 'City', 'Procedure', 'State', 'Treatment_Charge']
            headers = [i.strip() for i in patientsfile.columns.tolist()]
            if  headers != correct_headers:
                for i,j in zip(headers, correct_headers):
                    if i!=j:
                        messages.error(request, f"Column {i} and Column {j} do not match!", extra_tags="headers_mismatch" )
                        break
                return render(request, "dedupeapp/home.html", {})

            #Replacing Missing Values with a single constant value
            patientsfile['Name'].fillna('No Name', inplace=True)
            patientsfile['Address'].fillna('No Address', inplace=True)
            patientsfile['City'].fillna('No City', inplace=True)
            patientsfile['Procedure'].fillna('No Procedure', inplace=True)
            patientsfile['State'].fillna('No State', inplace=True)
            patientsfile['Treatment_Charge'].fillna(0, inplace=True)

            df_hospitalinpatients = patientsfile.set_index('Patient_ID')
            num_records = len(df_hospitalinpatients)

            #Making Record Pairs!!!

            #Building the indexer
            indexer = recordlinkage.Index()
            indexer.block(left_on='State')

            patient_pairs = indexer.index(df_hospitalinpatients)
            created_pairs = len(patient_pairs)

            print(num_records)

            compareDFcolumns = recordlinkage.Compare()
            compareDFcolumns.string('Name', 'Name', method='jarowinkler', threshold=0.85, label='Name')
            compareDFcolumns.string('Address', 'Address', method='jarowinkler', threshold=0.85, label='Address')
            compareDFcolumns.string('City', 'City', method='levenshtein', threshold=0.85, label='City')

            inpatient_features = compareDFcolumns.compute(patient_pairs, df_hospitalinpatients)
                
            predictions = nb_predictions.predict(inpatient_features)

            num_predictions = len(predictions)

            if num_predictions == 0:
                messages.error(request, f"No more duplicates found!!!!!!!!" )
                return render(request, "dedupeapp/home.html", {})
            else:
                #print(predictions)

                dedupedlist = []

                for i in predictions:

                    df = df_hospitalinpatients[df_hospitalinpatients.index.isin([i[0], i[1]])]
                    json_records = df.reset_index().to_json(orient ='records')
                    temp_dup_pairs = json.loads(json_records)
                    dup_pairs.append(temp_dup_pairs[0])
                    dup_pairs.append(temp_dup_pairs[1])



                    # print(temp_dup_pairs[0]['Patient_ID'])

                    for a in temp_dup_pairs:
                        # print('XXXXXXXXXXXXXXXXXXX', dedupedlist[0]) 

                        data = {
                            'Patient_ID' : None,
                            'Name' : None,
                            'Address' : None,
                            'City': None,
                            'Procedure': None,
                            'State': None,
                            'Treatment_Charge': None
                        }

                        if len(str(temp_dup_pairs[0]['Patient_ID'])) == len(str(temp_dup_pairs[1]['Patient_ID'])):
                            data['Patient_ID'] = temp_dup_pairs[0]['Patient_ID']
                        else:
                            data['Patient_ID'] = temp_dup_pairs[1]['Patient_ID']

                        if len(temp_dup_pairs[0]['Name']) > len(temp_dup_pairs[1]['Name']):
                            data['Name'] = temp_dup_pairs[0]['Name']
                        else:
                            data['Name'] = temp_dup_pairs[1]['Name']
                            
                        if len(temp_dup_pairs[0]['Address']) > len(temp_dup_pairs[1]['Address']):
                            data['Address'] = temp_dup_pairs[0]['Address']
                        else:
                            data['Address'] = temp_dup_pairs[1]['Address']

                        if len(temp_dup_pairs[0]['City']) > len(temp_dup_pairs[1]['City']):
                            data['City'] = temp_dup_pairs[0]['City']
                        else:
                            data['City'] = temp_dup_pairs[1]['City']
                            
                        if len(temp_dup_pairs[0]['Procedure']) > len(temp_dup_pairs[1]['Procedure']):
                            data['Procedure'] = temp_dup_pairs[0]['Procedure']
                        else:
                            data['Procedure'] = temp_dup_pairs[1]['Procedure']

                        if len(temp_dup_pairs[0]['State']) > len(temp_dup_pairs[1]['State']):
                            data['State'] = temp_dup_pairs[0]['State']
                        else:
                            data['State'] = temp_dup_pairs[1]['State']
                            
                        if len(str(temp_dup_pairs[0]['Treatment_Charge'])) > len(str(temp_dup_pairs[1]['Treatment_Charge'])):
                            data['Treatment_Charge'] = temp_dup_pairs[0]['Treatment_Charge']
                        else:
                            data['Treatment_Charge'] = temp_dup_pairs[1]['Treatment_Charge']
                            
                    dedupedlist.append(data)

                # print(dedupedlist)

                df_zero = pd.DataFrame(dedupedlist)

                df_zero = df_zero.set_index('Patient_ID')

                print(df_zero)

            # for r in dedupedlist:
                #    print(r)
                    
                drop_values = [x[0] for x in predictions]
                drop_values1 = [a[1] for a in predictions]

                #print(drop_values)

                #Droppping rows that contain any value in the list
                dropped1 = df_hospitalinpatients[df_hospitalinpatients.index.isin(drop_values) == False]
                dropped2 = dropped1[dropped1.index.isin(drop_values1) == False]

                print(dropped2)
                    
                title = "Dedupedfile" + format(pd.datetime.now().strftime("%Y-%m-%d %Hh%Mm%Ss"))

                deduped_hospitalinpatients = dropped2.append(df_zero)
                    
                x = deduped_hospitalinpatients.to_csv()
                f = ContentFile(x.encode('utf-8'))

                object= Deduped.objects.create(title=title, user=request.user)
                object.deduped_file.save(f'{title}.csv', f)
                object.save()

                deduped_set = Deduped.objects.filter(id=object.id)

        context = {
            'dup_pairs' : dup_pairs,
            'num_records': num_records,
            'created_pairs' : created_pairs,
            'num_predictions' : num_predictions,
            'deduped_set': deduped_set
        }
        
        # return redirect('dedupe_results') 
        return render(request, "dedupeapp/dedupe_results.html", context)

# Create your views here.

class DataTable(ListView):
    template_name = 'dedupeapp/get_results.html'
    login_url = settings.LOGIN_URL
    model =  Deduped

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={"objects_list": self.model.objects.filter(user=request.user)})

class DeletView(View):
    template_name = 'dedupeapp/get_results.html'
    login_url = settings.LOGIN_URL
    model =  Deduped



    def get(self, request, *args, **kwargs):
        self.model.objects.filter(id=kwargs.get('id')).delete()
        return render(request, self.template_name, context={"objects_list": self.model.objects.filter(user=request.user)})
