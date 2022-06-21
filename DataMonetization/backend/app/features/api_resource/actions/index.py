import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.helpers.action import action_response
from app.helpers.current_user import get_current_user

from app.helpers.database.mongo import str_to_id

from app.helpers.http.response import report_not_found_error
from app.helpers.http.response import report_forbidden_error

from app.services.api_resource.get_by_api import get_by_api
from app.services.api.get_by_id import get_api_by_id

from .__index_params import parameters

route = router.routes["get API resources"]
route.set_parameters(parameters)

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, params={"src": "query", "defns": parameters}, user_roles=route.roles)
def index_resources(api_id, offset, limit, **kwargs):
  api = get_api_by_id(api_id)
  current_user = get_current_user()

  if api.owner.id != current_user.id:
    report_forbidden_error()

  resources = [x.to_dict() for x in get_by_api(api)]
  return action_response({"data": resources[offset:limit]})