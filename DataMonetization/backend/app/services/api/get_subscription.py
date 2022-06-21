from app.models.api_subscription import APISubscription
from app.helpers.time import get_current_time
from app.helpers.http.response import report_not_found_error

def get_subscription(user, api):
  previous = APISubscription.objects(user_id=str(user.id), api_id=str(api.id), requests__gte=1).order_by("-expires_at").first()
  if previous:
    if previous.expires_at < get_current_time():
      report_not_found_error("you have no active subscription to the API (old one expired)")
    else:
      return previous
  else:
    report_not_found_error("you have no active subscription to the API")