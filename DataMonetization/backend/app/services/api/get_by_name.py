from app.models.api import API
from app.helpers.http.response import report_not_found_error

def get_api_by_name(api_name):
  api = API.objects(name=api_name).first()
  if not api:
    report_not_found_error(f"API not found: {api_name}")
  return api