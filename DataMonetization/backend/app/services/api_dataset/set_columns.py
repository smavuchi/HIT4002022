from app.services.api_dataset.get_dataframe import get_dataframe
from app.services.api_dataset.save_dataframe import save_dataframe
from app.services.api_dataset.update_info import update_dataset_info

def set_columns(dataset, needed_columns):
  df = get_dataframe(dataset)
  columns_to_drop = [x for x in list(df.columns) if x not in needed_columns]
  df.drop(columns_to_drop, axis=1, inplace=True)
  save_dataframe(dataset, df)

  id_columns = dataset.id_columns

  for column in id_columns:
    if column not in df.columns:
      id_columns = [x for x in id_columns if x != column]

  dataset.id_columns = id_columns
  dataset.save()

  return update_dataset_info(dataset)