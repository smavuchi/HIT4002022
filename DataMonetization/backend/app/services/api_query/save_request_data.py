import flask
from app.helpers.models import Model

from app.services.api.should_have_active_subscription import should_have_active_subscription
from app.models.api_request import APIRequest

def save_request_data(user, api):
  # ensure user has a subscription
  subscription = should_have_active_subscription(user, api)

  # reduce the available requests by 1
  subscription.requests = subscription.requests - 1
  subscription.save()

  created, item = Model.create(APIRequest, 
    url=flask.request.url, 
    endpoint=flask.request.path,
    api_id=str(api.id),
    user_id=str(user.id),
    request_headers=dict(flask.request.headers))
