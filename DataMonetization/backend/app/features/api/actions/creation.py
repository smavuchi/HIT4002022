import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.services.api.create import create_api as _create_api
from app.helpers.action import action_response
from app.helpers.current_user import get_current_user

from .__creation_params import parameters

route = router.routes["create api"]
route.set_parameters(parameters)

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, params={"src": "json", "defns": parameters}, user_roles=route.roles)
def create_api(**kwargs):
  current_user = get_current_user()
  result = _create_api(owner=current_user, owner_email=current_user.email, **kwargs)
  return action_response({"data": result.to_dict()})