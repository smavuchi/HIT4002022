from app.helpers.http.response import report_forbidden_error

def should_belong_to_api(resource, api):
  if resource.api_id != str(api.id):
    report_forbidden_error("resource does not belong to API")