import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.services.authentication.oauth.facebook import authenticate

from app.helpers.action import action_response

from .__facebook_oauth_auth_params import parameters

route = router.routes["facebook oauth"]
route.set_parameters(parameters)

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, params={"src": "json", "defns": parameters})
def facebook_oauth_authentication(token, returns, **kwargs):
  data = authenticate(token, returns)
  return action_response({ "data": data })