from app.services.api_dataset.delete_api_dataset import delete_api_dataset
from app.services.api_dataset.delete import delete_dataset
from app.services.api.get_by_id import get_api_by_id

def delete_resource(resource):
  try:
    delete_api_dataset(str(resource.id))
  except:
    pass

  resource.delete()