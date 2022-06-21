from app.services.api_dataset.get_dataframe import get_dataframe
from app.services.api_dataset.save_dataframe import save_dataframe
from app.services.api_dataset.update_info import update_dataset_info

def get_percentage_missing_values_by_column(df):
  return df.isna().mean()

def drop_columns_with_min_percentage_missing_values(df, value):
  pct_missing = get_percentage_missing_values_by_column(df)
  df_less_missing_cols = df.loc[:, pct_missing < value/100].copy() 
  return df_less_missing_cols

def drop_columns_with_missing_values(dataset, min_percent=None):
  df = get_dataframe(dataset)

  if min_percent:
    df = drop_columns_with_min_percentage_missing_values(df, min_percent)

  # if max_percent:
  #   df = drop_columns_with_max_percentage_missing_values(df, max_percent)

  save_dataframe(dataset, df)
  return update_dataset_info(dataset)