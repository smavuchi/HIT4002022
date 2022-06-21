import os
import flask
import time

from werkzeug.utils import secure_filename
from app.helpers.http.response import report_internal_server_error

def save_file(file):
  upload_folder = flask.current_app.config["UPLOAD_DIR"]
  filename = secure_filename(file.filename)

  try:
    disk_filename = "%s_%s" % (str(time.time()), filename)
    file.save(os.path.join(upload_folder, disk_filename))
  except Exception as e:
    report_internal_server_error(f"could not save file '{filename}'. Reason: {str(e)}")

  return disk_filename