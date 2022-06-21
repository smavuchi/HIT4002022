from app.helpers.http.response import report_forbidden_error

def should_be_published(api):
  if not api.published:
    report_forbidden_error("API is not published yet")