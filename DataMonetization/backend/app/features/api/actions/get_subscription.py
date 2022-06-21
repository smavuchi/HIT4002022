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
from app.services.api.get_subscription import get_subscription
from app.services.api_package.get_by_id import get_api_package_by_id 

route = router.routes["gets an API subscription"]

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, user_roles=route.roles)
def show_api_subscription_for_user(api_id, **kwargs):
  current_user = get_current_user()
  api = get_api_by_id(api_id)

  if api.owner.id != current_user.id:
    if not api.published:
      report_forbidden_error("api has not been published yet")

  data = get_subscription(api=api, user=current_user).to_dict()

  for package in api.packages:
    if str(package.id) == data["package_id"]:
      data["package"] = package.to_dict(only=["name", "id", "requests", "pricing", "description"])
      del data["package_id"]
      return action_response({"data": data})

  report_internal_server_error(f"package not found: {data['package']}")