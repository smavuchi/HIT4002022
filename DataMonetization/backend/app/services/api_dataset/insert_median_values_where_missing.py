from app.services.api_dataset.get_dataframe import get_dataframe
from app.services.api_dataset.save_dataframe import save_dataframe
from app.services.api_dataset.update_info import update_dataset_info

def insert_medians_for_missing_values(df):
  numeric_cols = list(df.select_dtypes(include=['number']).columns)

  df_copy = df.copy()
  med = df_copy[numeric_cols].median()
  df_copy[numeric_cols] = df_copy[numeric_cols].fillna(med)

  return df_copy 

def insert_median_values_where_missing(dataset):
  df = get_dataframe(dataset)
  df = insert_medians_for_missing_values(df)
  save_dataframe(dataset, df)
  return update_dataset_info(dataset)