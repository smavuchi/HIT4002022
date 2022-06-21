from app.helpers.http.response import report_forbidden_error

def should_own_api(user, api):
  if str(api.owner.id) != str(user.id):
    report_forbidden_error()