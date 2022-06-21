from app.models.api_dataset import APIDataset
from app.helpers.database.mongo import str_to_id
from app.helpers.http.response import report_not_found_error

def find_dataset_by_id(dataset_id):
  item = APIDataset.objects(id=str_to_id(dataset_id)).first()
  if not item:
    report_not_found_error("api dataset not found")
  return item
