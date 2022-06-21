import os
import flask

def get_file_path(name):
  upload_folder = flask.current_app.config["UPLOAD_DIR"]
  return os.path.join(upload_folder, name)