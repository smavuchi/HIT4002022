from app.services.api_dataset.get_dataframe import get_dataframe

def get_missing_values_by_row(dataset):
  df = get_dataframe(dataset)
  items =  dict(df.isna().sum(axis='columns'))

  return {int(row): int(items[row]) for row in items}