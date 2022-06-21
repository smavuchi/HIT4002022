import os
import flask

from app.helpers.http.response import report_internal_server_error

def download_file(disk_filename):
  upload_folder = flask.current_app.config["UPLOAD_DIR"]

  try:
    return flask.send_file(os.path.join(upload_folder, disk_filename))
  except Exception as e:
    report_internal_server_error(f"could not download file '{filename}'. Reason: {str(e)}")