from app.services.api_dataset.get_dataframe import get_dataframe
from app.services.api_dataset.save_dataframe import save_dataframe
from app.services.api_dataset.update_info import update_dataset_info

def set_id_columns(dataset, columns):
  dataset.id_columns = columns
  dataset.save()
  return update_dataset_info(dataset)