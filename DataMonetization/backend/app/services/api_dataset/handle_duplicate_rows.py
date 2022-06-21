from app.services.api_dataset.get_dataframe import get_dataframe
from app.services.api_dataset.save_dataframe import save_dataframe
from app.services.api_dataset.update_info import update_dataset_info

def handle_duplicated_rows(dataset):
  df = get_dataframe(dataset)
  df = df.drop_duplicates(subset=[x for x in dataset.column_types if x not in dataset.id_columns], keep="first")
  save_dataframe(dataset, df)
  return update_dataset_info(dataset)