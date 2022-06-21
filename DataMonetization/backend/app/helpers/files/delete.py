import os
import flask

from app.helpers.http.response import report_internal_server_error

def delete_file(disk_filename):
  upload_folder = flask.current_app.config["UPLOAD_DIR"]

  try:
    os.remove(os.path.join(upload_folder, disk_filename))
  except Exception as e:
    report_internal_server_error(f"could not delete file '{disk_filename}'. Reason: {str(e)}")