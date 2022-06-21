from app.helpers.http.response import report_bad_request_error
from app.helpers.models import Model

def update_api(api, **kwargs):
  modified, result = Model.modify(api, **kwargs)

  if not modified:
    report_bad_request_error(result)

  return result