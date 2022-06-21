from app.services.api_dataset.get_dataframe import get_dataframe

def get_data(dataset, offset, limit):
  df = get_dataframe(dataset)
  return df[offset:offset+limit].to_json(orient="records")