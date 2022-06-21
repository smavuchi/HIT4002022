from app.models.api_resource import APIResource
from app.helpers.database.mongo import str_to_id
from app.helpers.http.response import report_not_found_error

def get_resource_by_name(name):
  item = APIResource.objects(name=name).first()

  if not item:
    report_not_found_error(f"API resource not found: {name}")

  return item