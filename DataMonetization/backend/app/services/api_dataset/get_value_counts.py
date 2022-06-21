from app.services.api_dataset.get_dataframe import get_dataframe

def _get_value_counts_for_column(df, column):
  return list(df[column].value_counts())

def get_value_counts_for_column(dataset, column):
  df = get_dataframe(dataset)
  return _get_value_counts_for_column(df, column)

def get_value_counts_for_columns(dataset):
  df = get_dataframe(dataset)
  counts = {}
  for column in df.columns:
    counts[column] = _get_value_counts_for_column(df, column)
  return counts