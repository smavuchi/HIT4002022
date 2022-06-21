import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.helpers.action import action_response
from app.helpers.current_user import get_current_user

from app.services.user.business_today import get_user_business_today

route = router.routes["current user business today"]

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, user_roles=route.roles)
def current_user_business_today(**kwargs):
  user = get_current_user()
  result = get_user_business_today(user)
  return action_response({"data": result})