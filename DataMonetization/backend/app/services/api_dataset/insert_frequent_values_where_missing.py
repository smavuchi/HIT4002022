from app.services.api_dataset.get_dataframe import get_dataframe
from app.services.api_dataset.save_dataframe import save_dataframe
from app.services.api_dataset.update_info import update_dataset_info

def insert_frequent_values_for_missing_nonnumeric_values(df):
  non_numeric_cols = list(df.select_dtypes(exclude=['number']).columns)

  df_copy = df.copy()
  most_freq = df_copy[non_numeric_cols].describe().loc['top']
  df_copy[non_numeric_cols] = df_copy[non_numeric_cols].fillna(most_freq)

  return df_copy 

def insert_frequent_values_where_missing(dataset):
  df = get_dataframe(dataset)
  df = insert_frequent_values_for_missing_nonnumeric_values(df)
  save_dataframe(dataset, df)
  return update_dataset_info(dataset)