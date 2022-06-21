from app.helpers.http.response import report_bad_request_error
from app.helpers.http.response import report_not_found_error

from app.helpers.models import Model
from app.helpers.database.mongo import str_to_id

from app.services.api_resource.get_by_id import get_api_resource_by_id
from app.services.api_resource.delete_resource import delete_resource

def delete_api_resource(api, resource):
  modified, result = Model.modify(api, resources=list(filter(lambda x: x.id != resource.id, api.resources)))

  if not modified:
    report_bad_request_error(result)

  delete_resource(resource)