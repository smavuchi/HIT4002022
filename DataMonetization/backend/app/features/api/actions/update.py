import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.helpers.action import action_response
from app.helpers.current_user import get_current_user

from app.services.api.get_by_id import get_api_by_id
from app.services.api.update import update_api as _update_api

from app.helpers.http.response import report_not_found_error
from app.helpers.http.response import report_forbidden_error

from .__update_params import parameters

route = router.routes["update api"]
route.set_parameters(parameters)

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, params={"src": "json", "defns": parameters}, user_roles=route.roles)
def update_api(api_id, **kwargs):
  current_user = get_current_user()
  api = get_api_by_id(api_id)

  if api.owner.id != current_user.id:
    report_forbidden_error("you can only update your own APIs")

  result = _update_api(api, **kwargs)
  return action_response({"data": result.to_dict()})