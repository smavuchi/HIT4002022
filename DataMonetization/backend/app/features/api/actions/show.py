import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.helpers.action import action_response
from app.helpers.current_user import get_current_user

from app.helpers.http.response import report_not_found_error
from app.helpers.http.response import report_forbidden_error

from app.services.api.get_by_id import get_api_by_id
from app.models.api_subscription import APISubscription

route = router.routes["get an api"]

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, user_roles=route.roles)
def show_api(api_id, **kwargs):
  current_user = get_current_user()
  api = get_api_by_id(api_id)

  if api.owner.id != current_user.id:
    if not api.published:
      report_forbidden_error("api has not been published yet")

  result = api.to_dict()
  result["subscribed"] = False

  if APISubscription.objects(api_id=api_id, user_id=str(current_user.id)).first():
    result["subscribed"] = True

  return action_response({"data": result})