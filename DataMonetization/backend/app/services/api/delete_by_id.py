from app.models.api import API
from app.services.api.find_by_id import find_api_by_id
from app.services.api.delete_api import delete_api

def delete_api_by_id(api_id):
  api = find_api_by_id(str(api_id))

  if not api:
    report_not_found_error("api not found: ", str(api_id))

  return delete_api(api)