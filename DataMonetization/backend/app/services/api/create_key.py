import flask
import secrets
from app.models.api_subscription import APISubscription

from app.helpers.http.response import report_bad_request_error
from app.helpers.http.response import report_forbidden_error
from app.helpers.models import Model

def create_api_key(api, user):
  subscription = APISubscription.objects(user__id=user.id, api_package__api__id=api.id, active=True).first()

  if not subscription:
    report_forbidden_error("no active subscription")

  api_key = secrets.token_urlsafe(20)
  modified, result = Model.modify(subscription, api_key=api_key)

  if not modified:
    report_bad_request_error(result)

  return result.api_key