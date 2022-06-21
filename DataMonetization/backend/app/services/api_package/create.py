import flask
from app.models.api import APIPackage

from app.helpers.http.response import report_bad_request_error
from app.helpers.http.response import report_forbidden_error
from app.helpers.http.response import report_internal_server_error

from app.services.api_package.get_by_name import get_api_package_by_name
from app.helpers.models import Model

def create_api_package(api, **attributes):
  package = get_api_package_by_name(api, attributes.get("name"))

  if package:
    report_forbidden_error("name already taken")

  created, package = Model.create(APIPackage, 
    api_id=str(api.id), 
    **attributes)

  if not created:
    report_bad_request_error(package)

  modified, result = Model.modify(api, add_to_set__packages=package)

  if not modified:
    report_internal_server_error(result)

  return package