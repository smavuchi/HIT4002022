import datetime

from app.helpers.models import Model
from app.models.api_subscription import APISubscription
from app.helpers.time import get_current_time
from app.helpers.http.response import report_forbidden_error
from app.helpers.http.response import report_internal_server_error

def subscribe_to_api_package(api, user, package):
  previous = APISubscription.objects(user_id=str(user.id), api_id=str(api.id)).order_by("-expires_at").first()

  if previous and previous.expires_at > get_current_time() and previous.requests > 0:
    report_forbidden_error("Your subscription has not yet expired")

  created, subscription = Model.create(APISubscription, 
    api_id=str(api.id),
    package_id=str(package.id),
    user_id=str(user.id),
    requests=package.requests,
    paid=package.pricing,
    expires_at=datetime.datetime.utcnow() + datetime.timedelta(days=30))

  if not created:
    report_internal_server_error("could not create subscription")

  return subscription