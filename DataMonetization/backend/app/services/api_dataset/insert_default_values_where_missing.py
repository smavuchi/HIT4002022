from app.services.api_dataset.get_dataframe import get_dataframe
from app.services.api_dataset.save_dataframe import save_dataframe
from app.services.api_dataset.update_info import update_dataset_info

def insert_defaults_for_missing_values(df, numeric, nonnumeric):
  numeric_cols = list(df.select_dtypes(include=['number']).columns)
  non_numeric_cols = list(df.select_dtypes(exclude=['number']).columns)

  df[numeric_cols] = df[numeric_cols].fillna(numeric)
  df[non_numeric_cols] = df[non_numeric_cols].fillna(nonnumeric)

  return df

def insert_default_values_where_missing(dataset, numeric=0, nonnumeric="__MISSING__"):
  df = get_dataframe(dataset)
  df = insert_defaults_for_missing_values(df, numeric, nonnumeric)
  save_dataframe(dataset, df)
  return update_dataset_info(dataset)