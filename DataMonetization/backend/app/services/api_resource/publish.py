import datetime

from app.helpers.http.response import report_bad_request_error
from app.helpers.models import Model

def publish_api_resource(resource):
  modified, result = Model.modify(
    resource, 
    published=not resource.published, 
    published_at=datetime.datetime.utcnow() if not resource.published else None)

  if not modified:
    report_bad_request_error(result)

  return result