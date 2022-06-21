import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.helpers.action import action_response
from app.helpers.current_user import get_current_user

from app.helpers.http.response import report_not_found_error
from app.helpers.http.response import report_forbidden_error
from app.helpers.http.response import report_internal_server_error

from app.services.api.get_by_id import get_api_by_id
from app.services.user.get_subscriptions import get_subscriptions

route = router.routes["get user subscriptions"]

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, user_roles=route.roles)
def show_subscriptions_for_user(**kwargs):
  current_user = get_current_user()
  data = get_subscriptions(str(current_user.id))
  return action_response({ "data": data })