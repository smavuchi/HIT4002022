from app.helpers.http.response import report_forbidden_error

def should_be_published(resource):
  if not resource.published:
    report_forbidden_error("API resource is not published yet")