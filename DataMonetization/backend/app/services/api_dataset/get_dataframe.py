import pandas as pd
from app.helpers.files import get_file_path

def get_dataframe(dataset):
  return pd.read_csv(get_file_path(dataset.filename))