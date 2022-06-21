import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.services.user.forgot_password import forgot_password as _forgot_password
from app.helpers.action import action_response

from .__forgot_password_params import parameters

route = router.routes["forgot user password"]
route.set_parameters(parameters)

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, params={"src": "json", "defns": parameters})
def forgot_password(email, username, phone, **kwargs):
  result = _forgot_password(email=email, username=username, phone=phone)
  return action_response(None)