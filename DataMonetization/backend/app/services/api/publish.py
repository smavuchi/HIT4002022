import datetime

from app.helpers.http.response import report_bad_request_error
from app.helpers.models import Model

def publish_api(api):
  modified, result = Model.modify(
    api, 
    published=not api.published,
    published_at=datetime.datetime.utcnow() if not api.published else None)

  if not modified:
    report_bad_request_error(result)