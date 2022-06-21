from app.helpers.models import Model
from app.services.api_dataset.get_by_resource_id import get_dataset_by_resource_id
from app.services.api_dataset.delete import delete_dataset

def delete_api_dataset(resource_id):
  dataset = get_dataset_by_resource_id(resource_id)
  delete_dataset(dataset)