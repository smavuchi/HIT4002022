from app.services.api_dataset.get_dataframe import get_dataframe

def get_missing_values(dataset):
  df = get_dataframe(dataset)
  return dict(df.isna().sum())