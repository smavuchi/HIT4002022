import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.services.user.delete_by_id import delete_user_by_id
from app.helpers.action import action_response
from app.helpers.current_user import get_current_user

route = router.routes["delete current user"]

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware)
def delete_self(**kwargs):
  current_user = get_current_user()
  result = delete_user_by_id(str(current_user.id))
  return action_response(None)