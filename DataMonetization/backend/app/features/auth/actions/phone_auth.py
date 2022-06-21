import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.services.authentication.phone import authenticate

from app.helpers.http.response import report_bad_request_error
from app.helpers.action import action_response

from .__phone_auth_params import parameters

route = router.routes["phone-password auth"]
route.set_parameters(parameters)

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, params={"src": "json", "defns": parameters})
def phone_authentication(phone, password, returns, **kwargs):
  data = authenticate(phone, password, returns)
  return action_response({ "data": data })