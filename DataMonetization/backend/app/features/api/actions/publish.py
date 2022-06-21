import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.helpers.action import action_response
from app.helpers.current_user import get_current_user

from app.helpers.http.response import report_not_found_error
from app.helpers.http.response import report_forbidden_error
from app.services.api.get_by_id import get_api_by_id
from app.services.api.publish import publish_api as _publish_api

route = router.routes["publish an api"]

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, user_roles=route.roles)
def publish_api(api_id, **kwargs):
  current_user = get_current_user()
  api = get_api_by_id(api_id)

  if api.owner.id != current_user.id:
    report_forbidden_error("you can only publish your own APIs")

  _publish_api(api)
  return action_response()