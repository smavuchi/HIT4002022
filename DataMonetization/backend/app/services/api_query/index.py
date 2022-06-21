from app.helpers.http.response import report_forbidden_error
from app.services.api_dataset.get_dataframe import get_dataframe
from app.services.api_dataset.get_by_resource_id import get_dataset_by_resource_id

def index_api_resource(resource, offset, limit, columns):
  dataset = get_dataset_by_resource_id(str(resource.id), throw=False)

  if not dataset:
    report_forbidden_error("resource has no associated dataset")

  df = get_dataframe(dataset)
  dataset_columns = []

  if columns:
    for column in columns:
      if column in df.columns:
        dataset_columns.append(column)
      else:
        report_bad_request_error(f"column does not exist on dataset: {column}")
  else:
    dataset_columns = list(df.columns)

  result = []

  for row in df.values[offset:limit]:
    item = {}

    for i in range(len(dataset_columns)):
      column = dataset_columns[i]
      item[column] = list(row)[i]

    result.append(item)

  return result