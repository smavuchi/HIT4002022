from app.helpers.database.mongo import str_to_id
from app.models.api_package import APIPackage

def get_api_package_by_name(api, name):
  return APIPackage.objects(api_id=str(api.id), name=name).first()