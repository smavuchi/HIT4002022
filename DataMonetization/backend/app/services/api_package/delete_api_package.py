from app.helpers.http.response import report_bad_request_error
from app.helpers.models import Model

from app.services.api_package.delete import delete_package

def delete_api_package(api, package):
  modified, result = Model.modify(api, packages=list(filter(lambda x: str(x.id) != str(package.id), api.packages)))

  if not modified:
    report_bad_request_error(result)

  delete_package(package)