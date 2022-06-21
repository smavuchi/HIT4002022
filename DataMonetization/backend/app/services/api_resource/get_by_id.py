from app.models.api_resource import APIResource
from app.helpers.database.mongo import str_to_id
from app.helpers.http.response import report_not_found_error

def get_api_resource_by_id(resource_id):
  item = APIResource.objects(id=str_to_id(resource_id)).first()

  if not item:
    report_not_found_error(f"api resource not found: {resource_id}")

  return item