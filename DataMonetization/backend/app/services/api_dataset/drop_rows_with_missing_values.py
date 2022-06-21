from app.services.api_dataset.get_dataframe import get_dataframe
from app.services.api_dataset.save_dataframe import save_dataframe
from app.services.api_dataset.update_info import update_dataset_info

def get_missing_values_by_row(df):
  return df.isna().sum(axis='columns')

def keep_rows_with_min_missing_values(df, value):
  missing_by_row = get_missing_values_by_row(df)
  return df[missing_by_row < value].copy()

# def keep_rows_with_max_missing_values(df, value):
#   missing_by_row = get_missing_values_by_row(df)
#   return df[missing_by_row < value].copy()

def drop_rows_with_missing_values(dataset, _min=None):
  df = get_dataframe(dataset)

  if _min:
    df = keep_rows_with_min_missing_values(df, _min)

  # if _max:
  #   df = keep_rows_with_max_missing_values(df, _max)

  save_dataframe(dataset, df)
  return update_dataset_info(dataset)