import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.services.user.creation import create_user
from app.helpers.http.response import report_bad_request_error
from app.helpers.action import action_response

from .__registration_params import parameters

route = router.routes["register user"]
route.set_parameters(parameters)

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, params={"src": "json", "defns": parameters})
def register_user(password, confirmation_password, **kwargs):
  if password != confirmation_password:
    report_bad_request_error("password does not match confirmation")

  result = create_user(password=password, role="user", **kwargs)
  return action_response({"data": result.to_dict(only=["id", "email", "username"]), "status": 201})