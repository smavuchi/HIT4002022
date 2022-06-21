import pandas as pd

from app.helpers.time import get_current_time
from app.helpers.files import get_file_path
from app.services.api_dataset.get_dataframe import get_dataframe

def update_dataset_info(dataset):
  df = get_dataframe(dataset)
  columns = list(df.columns)
  numeric_columns = list(df.select_dtypes(include=['number']).columns)

  dataset_columns_description = {}
  dataset_kurt_per_column = {}
  dataset_percentage_missing_values_by_column = {}
  dataset_column_types = {}

  for column in columns:
    description = dict(df[column].describe())

    dataset_columns_description[column] = {
      "count": int(description.get("count", 0)),
      "mean": float(description.get("mean", 0)),
      "std": float(description.get("std", 0)),
      "min": float(description.get("min", 0)),
      "25%": float(description.get("25%", 0)),
      "50%": float(description.get("50%", 0)),
      "75%": float(description.get("75%", 0)),
      "max": float(description.get("max", 0)),
      "unique": int(description.get("unique", 0)),
      "top": str(description.get("top", "")),
      "freq": float(description.get("freq", 0)),
    }

    dataset_kurt_per_column[column] = float(df[column].kurt()) if column in numeric_columns else 0
    dataset_percentage_missing_values_by_column[column] = df[column].isna().mean()
    dataset_column_types[column] = str(df[column].dtype)

  dataset.columns_description = dataset_columns_description
  dataset.kurt_per_column = dataset_kurt_per_column
  dataset.percentage_missing_values_by_column = dataset_percentage_missing_values_by_column
  dataset.column_types = dataset_column_types

  dataset.modified_at = get_current_time()
  dataset.save()

  return dataset.reload()