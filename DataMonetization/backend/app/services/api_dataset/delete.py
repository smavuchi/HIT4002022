from app.helpers.http.response import report_bad_request_error
from app.helpers.files import delete_file

def delete_dataset(dataset):
  delete_file(dataset.filename)
  dataset.delete()