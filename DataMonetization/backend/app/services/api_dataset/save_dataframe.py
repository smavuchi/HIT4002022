from app.helpers.files import delete_file
from app.helpers.files import get_file_path

def save_dataframe(dataset, df):
  delete_file(dataset.filename)
  df.to_csv(get_file_path(dataset.filename), index=False)