from app.services.api_dataset.get_dataframe import get_dataframe
from app.services.api_dataset.save_dataframe import save_dataframe
from app.services.api_dataset.update_info import update_dataset_info

def set_column_types(dataset, column_types):
  df = get_dataframe(dataset)
  df = df.astype(column_types)
  save_dataframe(dataset, df)
  return update_dataset_info(dataset)