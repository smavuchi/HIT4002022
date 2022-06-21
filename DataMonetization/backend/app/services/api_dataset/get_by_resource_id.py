from app.models.api_dataset import APIDataset
from app.helpers.database.mongo import id_to_str
from app.helpers.http.response import report_not_found_error

def get_dataset_by_resource_id(resource_id, throw=True):
  item = APIDataset.objects(resource_id=id_to_str(resource_id)).first()
  if (not item) and throw:
    report_not_found_error(f"api dataset not found for resource: {resource_id}")
  return item
