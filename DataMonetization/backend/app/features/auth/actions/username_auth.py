import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.services.authentication.username import authenticate

from app.helpers.http.response import report_bad_request_error
from app.helpers.action import action_response

from .__username_auth_params import parameters

route = router.routes["username-password auth"]
route.set_parameters(parameters)

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, params={"src": "json", "defns": parameters})
def username_authentication(username, password, returns, **kwargs):
  data = authenticate(username, password, returns)
  return action_response({ "data": data })