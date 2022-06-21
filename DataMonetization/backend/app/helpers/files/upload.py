import flask

from app.helpers.http.response import report_bad_request_error
from app.helpers.http.response import report_internal_server_error
from werkzeug.utils import secure_filename

from .save import save_file

def upload_file(name, required=True):
  if name not in flask.request.files:
    if required:
      report_bad_request_error(f"missing required file: {name}")
    return False, "no file provided"

  file = flask.request.files[name]
  filename = secure_filename(file.filename)
  disk_filename = save_file(file)

  return True if filename else False, disk_filename
