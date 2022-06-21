import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.services.user.verification_email import send_verification_email as _send_verification_email
from app.helpers.http.response import report_bad_request_error
from app.helpers.action import action_response

from .__verification_email_params import parameters

route = router.routes["send verification email"]
route.set_parameters(parameters)

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, params={"src": "json", "defns": parameters})
def send_verification_email(email, **kwargs):
  result = _send_verification_email(email)
  return action_response(None)