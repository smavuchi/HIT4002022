from app.services.api_dataset.get_dataframe import get_dataframe

def get_nonnumeric_columns(dataset):
  df = get_dataframe(dataset)
  return list(df.select_dtypes(exclude=['number']).columns)