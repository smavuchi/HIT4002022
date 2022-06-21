from app.helpers.http.response import report_not_found_error
from app.models.api_package import APIPackage

def get_api_package_by_id(api, _id):
  item = APIPackage.objects(api_id=str(_id)).first()

  if not item:
    report_not_found_error("api package not found")

  return item