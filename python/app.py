from flask import Flask, request, send_file, send_from_directory
from flask_cors import CORS, cross_origin
from datetime import datetime
from flask import jsonify
import requests
import json
from werkzeug.utils import secure_filename
from pathlib import Path

app = Flask(__name__)
app.debug = True

# Cross Origin Stuff
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin'
# app.config['CORS_RESOURCES'] = {r"/*": {"origins": "*"}}
cors = CORS(app)

root = Path('.')

# save image
@app.route('/saveImage', methods=['POST'])
def saveImage():

    # get image
    image = request.files['image']
    image_filename = str(datetime.now()).replace('-', '')
    image_filename = image_filename.replace(':', '')
    image_filename = image_filename.replace('.', '')
    image_filename = image_filename.replace(' ', '-')
    image_filename = secure_filename(image_filename + '-' + image.filename)

    # save image to media directory
    file_path = root / 'media' / image_filename
    with open(file_path, 'wb') as f:
        f.write(image)
        f.close()
    
    return image_filename


# get image
@app.route('/media/<filename>', methods=['GET', 'POST'])
def media(filename):
    filename = secure_filename(filename)

    from pathlib import Path

    root = Path('.')

    folder_path = root / 'media'

    return send_from_directory(folder_path, filename, as_attachment=True)


# save image
@app.route('/faceMatch', methods=['POST'])
def faceMatch():

    # get image
    base64 = request.form['image']

    # get image extension from request data
    extension = request.form['image_extension']

    # save image base64 as decoded image file and return image filename
    from image_base64_to_image_file import image_base64_to_image_file
    image_filename = image_base64_to_image_file(base64, extension)

    # get unknown image path
    unknown_image_path = root / 'media' / image_filename

    # get known image path
    known_image_name = request.form['known_image']
    known_image_path = root / 'media' / known_image_name

    # perform facial recognition
    from facial_recognition import recognise_faces
    results = recognise_faces(known_image_path, unknown_image_path)

    return results


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # from waitress import serve
    # serve(app, host='0.0.0.0') # use waitress