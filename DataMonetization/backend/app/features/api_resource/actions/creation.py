import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.services.api_resource.create import create_api_resource as _create_api_resource
from app.helpers.action import action_response
from app.helpers.current_user import get_current_user

from app.services.api.get_by_id import get_api_by_id
from app.services.api.should_own_api import should_own_api

from .__creation_params import parameters

route = router.routes["create API resource"]
route.set_parameters(parameters)

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, params={"src": "json", "defns": parameters}, user_roles=route.roles)
def create_api_resource(api_id, **kwargs):
  current_user = get_current_user()
  
  api = get_api_by_id(api_id)
  should_own_api(current_user, api)

  result = _create_api_resource(api=api, **kwargs)
  return action_response({"data": result.to_dict()})