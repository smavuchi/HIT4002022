from app.services.api_dataset.get_dataframe import get_dataframe

def get_percentage_missing_values_by_column(dataset):
  df = get_dataframe(dataset)
  return dict(df.isna().mean())