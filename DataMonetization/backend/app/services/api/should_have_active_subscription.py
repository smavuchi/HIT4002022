from app.services.api.get_subscription import get_subscription
from app.helpers.http.response import report_forbidden_error

def should_have_active_subscription(user, api):
  try:
    return get_subscription(user, api)
  except:
    report_forbidden_error("You have no active subscription to the API")