import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.services.user.verification import verify_user as _verify_user
from app.helpers.http.response import report_bad_request_error
from app.helpers.action import action_response

from .__verification_params import parameters

route = router.routes["verify user"]
route.set_parameters(parameters)

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, params={"src": "json", "defns": parameters})
def verify_user(username, email, phone, code, **kwargs):
  result = _verify_user(username=username, email=email, phone=phone, code=code)
  return action_response(None)