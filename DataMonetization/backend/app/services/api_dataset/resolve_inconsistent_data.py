from app.services.api_dataset.get_dataframe import get_dataframe
from app.services.api_dataset.save_dataframe import save_dataframe
from app.services.api_dataset.update_info import update_dataset_info

def resolve_inconsistent_data(dataset):
  df = get_dataframe(dataset)

  # convert all strings to lowercase
  df = df.applymap(lambda s: s.lower() if type(s) == str else s)

  # remove whitespace from strings
  df = df.applymap(lambda s: s.strip() if type(s) == str else s)
  save_dataframe(dataset, df)

  return update_dataset_info(dataset)