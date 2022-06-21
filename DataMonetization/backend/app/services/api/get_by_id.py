from app.models.api import API
from app.models.api_subscription import APISubscription
from app.helpers.database.mongo import str_to_id
from app.helpers.http.response import report_not_found_error

def get_api_by_id(api_id):
  item = API.objects(id=str_to_id(api_id)).first()
  if not item:
    report_not_found_error(f"api not found: {api_id}")
  return item