from app.helpers.files import download_file

def download_dataset(dataset):
  return download_file(dataset.filename)