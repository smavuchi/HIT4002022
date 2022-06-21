import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.helpers.action import action_response
from app.helpers.current_user import get_current_user

from app.services.user.statistics import get_statistics

route = router.routes["current user statistics"]

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, user_roles=route.roles)
def current_user_statistics(**kwargs):
  user = get_current_user()
  result = get_statistics(user)
  return action_response({"data": result})