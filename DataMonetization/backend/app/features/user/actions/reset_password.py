import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.services.user.reset_password import reset_password as _reset_password
from app.helpers.http.response import report_bad_request_error
from app.helpers.action import action_response

from .__reset_password_params import parameters

route = router.routes["reset user password"]
route.set_parameters(parameters)

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, params={"src": "json", "defns": parameters})
def reset_password(username, email, phone, code, password, **kwargs):
  result = _reset_password(username=username, email=email, phone=phone, code=code, password=password)
  return action_response(None)