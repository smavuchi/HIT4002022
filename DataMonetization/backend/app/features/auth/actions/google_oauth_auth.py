import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.services.authentication.oauth.google import authenticate

from app.helpers.action import action_response

from .__google_oauth_auth_params import parameters

route = router.routes["google oauth"]
route.set_parameters(parameters)

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, params={"src": "json", "defns": parameters})
def google_oauth_authentication(token, returns, **kwargs):
  data = authenticate(token, returns)
  return action_response({ "data": data })