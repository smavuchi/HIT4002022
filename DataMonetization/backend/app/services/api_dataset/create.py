import flask
from app.models.api_dataset import APIDataset
from app.helpers.models import Model

from app.helpers.files import delete_file
from app.helpers.files import upload_file

from app.helpers.http.response import report_bad_request_error
from app.helpers.http.response import report_internal_server_error
from app.services.api_dataset.update_info import update_dataset_info
from app.services.api_dataset.delete_api_dataset import delete_api_dataset

def create_dataset(**attributes):
  try:
    delete_api_dataset(attributes["resource_id"])
  except:
    pass

  uploaded, filename = upload_file("dataset", required=True)
  created, dataset = Model.create(APIDataset, 
    filename=filename, 
    **attributes)

  if not created:
    delete_file(filename)
    report_bad_request_error(dataset)

  try:
    update_dataset_info(dataset)
  except Exception as e:
    delete_file(filename)
    dataset.delete()
    report_internal_server_error(f"could not save calculated dataset metadata. Reason: {str(e)}")

  return dataset