# from crypt import methods
# from crypt import methods
from prediction import plate_detect,plate_info,segment_characters,custom_f1score
import glob
import os
import re
from PIL import Image
from io import BytesIO
import base64
from pixel_image import pixelate_image, generate_pixel_image, classify_face, atkinson_dither
from werkzeug.utils import redirect, secure_filename
from datetime import datetime
import cv2
from flask import render_template, jsonify, Flask, redirect, url_for, request,session,flash
import pymongo
import bcrypt
import requests
import json
app = Flask(__name__)

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['carreg']
app = Flask(__name__)
app.secret_key = "detectform"

ALLOWED_EXTENSIONS = {'mp4'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


path = os.getcwd()
UPLOAD_FOLDER = os.path.join(path, 'static/uploads')
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

BASE_DIR = os.getcwd()
dir = os.path.join(BASE_DIR, "uploads")

for root, dirs, files in os.walk(dir):
    for file in files:
        path = os.path.join(dir, file)
        os.remove(path)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# MAIN APP MAKING

# Home Page


# @app.route('/')
# def index():
#     return render_template('index.html')

# Prediction - Vehicle Details Page


def convert_and_save(b64_string):
    with open(UPLOAD_FOLDER +"\\" + "imageToSave.jpg", "wb") as fh:
        fh.write(base64.decodebytes(b64_string.encode()))

@app.route('/process',methods=['POST'])
def process():

    input = request.json
    
    image_data = re.sub('^data:image/.+;base64,', '', input['img'])
    im = Image.open(BytesIO(base64.b64decode(image_data)))
    filename = secure_filename(im.filename)
    
    image_ascii = atkinson_dither(image_data)
    convert_and_save(image_data)
    inputImg = cv2.imread(UPLOAD_FOLDER +"\\" + "imageToSave.jpg")
    inpImg, plate = plate_detect(inputImg)
    print(plate)
    if len(plate) > 0:
        print("pay")
        pay="yes"
    else:
        pay="no"
        print('nothing')
        


    return pay


@app.route('/cardetail', methods=['POST'])
def upload_image():
    email = session["email"]
    global videoPath
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        videoPath = UPLOAD_FOLDER +"\\" + "imageToSave.jpg"
        uploaded_file.save(videoPath)
    
    print("running")

    try:
        url = "https://zyanyatech1-license-plate-recognition-v1.p.rapidapi.com/recognize_url"

        querystring = {"image_url":"https://203c-77-246-53-35.eu.ngrok.io/static/uploads/imageToSave.jpg"}

        headers = {
            "X-RapidAPI-Host": "zyanyatech1-license-plate-recognition-v1.p.rapidapi.com",
            "X-RapidAPI-Key": "861dfa1282mshf401b1d591d72c3p1b4842jsn1c00532698db"
        }

        response = requests.request("POST", url, headers=headers, params=querystring)
        # print(response.result)

        # print(response.text)
        data = response.text
        parse_json = json.loads(data)
        info = parse_json['results']
        print("Info about API:\n", info)
        number_plate= parse_json['results'][0]['plate']
        print("Info about API:\n",number_plate)
    except Exception:
                    flash('Can you upload a valid image','danger')
                    return render_template('index.html', email=email)

   
    # vehInfo = runVideo(videoPath)
    # print(vehInfo)
    print("still there")
    print(number_plate)
    # EMPTY UPLOAD FOLDER
    result=db.register.find_one({"carreg":number_plate})
    if result:
        owner=db.register.find_one({"carreg":number_plate},{"owner":1,"_id":0})
        balance=db.register.find_one({"carreg":number_plate},{"balance":1,"_id":0})
        if float(balance['balance'])>5:
            answ=float(balance['balance'])-5
            db.register.find_one_and_update({"carreg":number_plate},{'$set':{"balance":answ}})
            current = datetime.now()
            db.Transactions.insert_one({"owner":owner['owner'],"license":number_plate,"balance":answ,"initialbalance":balance['balance'],"deduction": 5,"transtime":current})
            print("done")
            return render_template("/carDetails.html",balance=answ,result=result, numberplate=number_plate,email=email)
        else:
            flash('You have insufficient Funds','danger')
            return render_template('index.html', email=email)
    
    else:
        flash('Vehicle not registered with us','danger')
        return render_template('index.html', email=email)

    
# @app.route('/uploadfeed', methods=['GET'])   
# def get_feed():

#     email = session["email"]
#     return render_template('index1.html', email=email)
   
@app.route('/uploadimage', methods=['GET'])   
def get_image():

    email = session["email"]
    return render_template('index.html', email=email)

@app.route('/uploadfeed', methods=['GET'])   
def get_feed():

    email = session["email"]
    return render_template('index1.html', email=email)

@app.route('/uploadvideo', methods=['GET'])   
def get_video():

    email = session["email"]
    return render_template('index3.html', email=email)
    

@app.route('/cardeta',methods=['POST'])
def runVideo():
    print("hello")
    email = session["email"]
    global videoPath
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        videoPath = UPLOAD_FOLDER +"\\" + "test.mp4"
        uploaded_file.save(videoPath)
    # license_video.mp4 have to be yours, I haven't uploaded for privacy concern
    cam = cv2.VideoCapture(UPLOAD_FOLDER +"\\" + "test.mp4")
    if cam.isOpened() == False:
        print("Video not imported")
        flash('No Video was uploaded','danger')
        return render_template('index3.html', email=email)

    
    while(cam.isOpened()):
        ret, frame = cam.read()
        if ret == True:
            cv2.imwrite(os.path.join( UPLOAD_FOLDER +"\\", 'Frame.jpg'), frame)
            # inputImg = cv2.imread(UPLOAD_FOLDER + "\\" + "Frame.jpg")
            # car_plate, plate_img = plate_detect(inputImg)
            # #cv2.imshow("License Video", car_plate)
            # if len(plate_img) > 0:
                
            #     try:
            #         plate_char = segment_characters(plate_img)
            #     except Exception:
            #         flash('Can you upload a valid image','danger')
            #         return render_template('index3.html', email=email)

            #     number_plate = plate_info(plate_char)
            #     print(number_plate)
            #     result=db.register.find_one({"carreg":number_plate})

            try:
                url = "https://zyanyatech1-license-plate-recognition-v1.p.rapidapi.com/recognize_url"

                querystring = {"image_url":"https://203c-77-246-53-35.eu.ngrok.io/static/uploads/Frame.jpg"}

                headers = {
                    "X-RapidAPI-Host": "zyanyatech1-license-plate-recognition-v1.p.rapidapi.com",
                    "X-RapidAPI-Key": "861dfa1282mshf401b1d591d72c3p1b4842jsn1c00532698db"
                }

                response = requests.request("POST", url, headers=headers, params=querystring)
                # print(response.result)

                # print(response.text)
                data = response.text
                parse_json = json.loads(data)
                info = parse_json['results']
                print("Info about API:\n", info)
                number_plate= parse_json['results'][0]['plate']
                print("Info about API:\n",number_plate)
                
            except Exception:
                    flash('Can you re-upload  valid video','danger')
                    return render_template('index3.html', email=email)

            result=db.register.find_one({"carreg":number_plate})

            if result:
                    owner=db.register.find_one({"carreg":number_plate},{"owner":1,"_id":0})
                    balance=db.register.find_one({"carreg":number_plate},{"balance":1,"_id":0})
                    if float(balance['balance'])>5:
                        answ=float(balance['balance'])-5
                        db.register.find_one_and_update({"carreg":number_plate},{'$set':{"balance":answ}})
                        current = datetime.now()
                        db.Transactions.insert_one({"owner":owner['owner'],"license":number_plate,"balance":answ,"initialbalance":balance['balance'],"deduction": 5,"transtime":current})
                        print("done")
                        cam.release()
                        cv2.destroyAllWindows()
                        return render_template("/carDetails1.html",balance=answ,result=result, numberplate=number_plate,email=email)
                    else:
                        flash('You have insufficient Funds','danger')
                        cam.release()
                        cv2.destroyAllWindows()
                        return render_template('index3.html', email=email)
    
            else:
                    flash('Vehicle not registered with us','danger')
                    cam.release()
                    cv2.destroyAllWindows()
                    return render_template('index3.html', email=email)
    
    
@app.route('/car', methods=['GET'])
def cardetails():
    email = session["email"]
    balance = request.args['balance']
    result = request.args['result']
    numberplate= request.args['numberplate']
    print(balance)

    return render_template("/carDetails.html",balance=balance,result=result,numberplate=numberplate,email=email)




@app.route('/cardetails', methods=['GET'])
def upload_live():
    print("running")
    email = session["email"]
    # inputImg = cv2.imread(UPLOAD_FOLDER +"\\" + "imageToSave.jpg")

    try:
        url = "https://zyanyatech1-license-plate-recognition-v1.p.rapidapi.com/recognize_url"

        querystring = {"image_url":"https://203c-77-246-53-35.eu.ngrok.io/static/uploads/imageToSave.jpg"}

        headers = {
            "X-RapidAPI-Host": "zyanyatech1-license-plate-recognition-v1.p.rapidapi.com",
            "X-RapidAPI-Key": "861dfa1282mshf401b1d591d72c3p1b4842jsn1c00532698db"
        }

        response = requests.request("POST", url, headers=headers, params=querystring)
        # print(response.result)

        # print(response.text)
        data = response.text
        parse_json = json.loads(data)
        info = parse_json['results']
        print("Info about API:\n", info)
        number_plate= parse_json['results'][0]['plate']
        print("Info about API:\n",number_plate)
    except Exception:
                    
                    flash('Can you upload a valid image','danger')
                    return render_template("/index1.html",email=email)
                    

    # inpImg, plate = plate_detect(inputImg)

    # try:
    #     plate_char = segment_characters(plate)
    
    # except Exception:
    #     flash('Can you upload a valid image','danger')
    #     return render_template('index1.html', email=email)
                
    # number_plate = plate_info(plate_char)

   
    # # vehInfo = runVideo(videoPath)
    # # print(vehInfo)
    # print("still there")
    # print(number_plate)
    # EMPTY UPLOAD FOLDER
    # BASE_DIR = os.getcwd()
    # dir = os.path.join(BASE_DIR, "uploads")

    # for root, dirs, files in os.walk(dir):
    #     for file in files:
    #         path = os.path.join(dir, file)
    #         os.remove(path)
    print("checking")
    result=db.register.find_one({"carreg":number_plate})
    if result:
        owner=db.register.find_one({"carreg":number_plate},{"owner":1,"_id":0})
        balance=db.register.find_one({"carreg":number_plate},{"balance":1,"_id":0})
        if float(balance['balance'])>5:
            answ=float(balance['balance'])-5
            db.register.find_one_and_update({"carreg":number_plate},{'$set':{"balance":answ}})
            current = datetime.now()
            db.Transactions.insert_one({"owner":owner['owner'],"license":number_plate,"balance":answ,"initialbalance":balance['balance'],"deduction": 5,"transtime":current})
            print("done")
            return render_template("/carDetails.html",balance=answ,result=result,email=email)
        else:
            flash('You have insufficient Funds','danger')
            return render_template("/index1.html",email=email)
            
    
    else:
        flash('Vehicle not registered with us','danger')
        return render_template("/index1.html",email=email)
            
    

@app.route('/signup', methods=['GET','POST'])
def index():
    message = ''
    #if method post in index
    if "email" in session:
        return redirect(url_for("logged_in"))
    if request.method == "POST":
        user = request.form.get("fullname")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        #if found in database showcase that it's found 
        user_found = db.users.find_one({"name": user})
        email_found = db.users.find_one({"email": email})
        if user_found:
            message = 'There already is a user by that name'
            return render_template('signup.html', message=message)
        if email_found:
            message = 'This email already exists in database'
            return render_template('signup.html', message=message)
        if password1 != password2:
            message = 'Passwords should match!'
            return render_template('signup.html', message=message)
        else:
            #hash the password and encode it
            hashed = bcrypt.hashpw(password2.encode('utf-8'), bcrypt.gensalt())
            #assing them in a dictionary in key value pairs
            user_input = {'name': user, 'email': email, 'password': hashed}
            #insert it in the record collection
            db.users.insert_one(user_input)
        
            
            #find the new created account and its email
            user_data = db.users.find_one({"email": email})
            new_email = user_data['email']
            #if registered redirect to logged in as the registered user
            return render_template('login.html', email=new_email)
    return render_template('signup.html')


@app.route('/logged_in')
def logged_in():
    if "email" in session:
        email = session["email"]
        return render_template('index2.html', email=email)
    else:
        return redirect(url_for("login"))

@app.route('/addvehicle',methods=['GET','POST'])
def addvehicle():
    if request.method=="POST":
        owner = request.form.get("fullname")
        email = request.form.get("email")
        carreg= request.form.get("carreg")
        vehicle = request.form.get("vname")
        carmodel = request.form.get("model")
        vehicletype = request.form.get("vtype")
        balance = request.form.get("balance")
        
        #if found in database showcase that it's found 
        print("running")
        email_found = db.register.find_one({"email": email})
        if email_found:
            flash('Account already inuse','danger')
            return render_template('account.html')

        else:
            car_details = {'owner': owner, 'email': email, 'carreg': carreg,'vehicle':vehicle,'carmodel':carmodel,'vehicletype':vehicletype,'balance':balance}
            db.register.insert_one(car_details)
            flash('Account created successfully','success')

            return redirect(url_for("addvehicle"))
    if "email" in session:
        email = session["email"]
        return render_template('account.html', email=email)
    






@app.route("/login", methods=["POST", "GET"])
def login():
    message = 'Please login to your account'
    if "email" in session:
        return redirect(url_for("logged_in"))

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        #check if email exists in database
        email_found = db.users.find_one({"email": email})
        if email_found:
            email_val = email_found['email']
            passwordcheck = email_found['password']
            #encode the password and check if it matches
            if bcrypt.checkpw(password.encode('utf-8'), passwordcheck):
                session["email"] = email_val
                return redirect(url_for('logged_in'))
            else:
                if "email" in session:
                    return redirect(url_for("logged_in"))
                message = 'Wrong password'
                return render_template('login.html', message=message)
        else:
            message = 'Email not found'
            return render_template('login.html', message=message)
    return render_template('login.html', message=message)

@app.route("/", methods=["POST", "GET"])
def home():
    return render_template('login.html')


@app.route("/logout", methods=["POST", "GET"])
def logout():
    if "email" in session:
        session.pop("email", None)
        return render_template("login.html")
    else:
        return render_template('login.html')

@app.route('/viewtrans')
def viewtrans():
    email = session["email"]

    trans=db.Transactions.find()
    print(trans)

    return render_template('transactions.html',trans=trans,email=email)

if __name__ == "__main__":
    app.run(debug=True)