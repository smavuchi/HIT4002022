import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.helpers.action import action_response
from app.helpers.current_user import get_current_user
from app.helpers.http.response import report_not_found_error

from app.services.api.get_by_id import get_api_by_id
from app.services.api.should_own_api import should_own_api

route = router.routes["get an API package"]

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, user_roles=route.roles)
def show_api_package(api_id, package_id, **kwargs):
  current_user = get_current_user()
  api = get_api_by_id(api_id)
  should_own_api(current_user, api)

  for package in api.packages:
    if str(package.id) == package_id:
      return action_response({"data": package.to_dict()})

  report_not_found_error(f"package not found: {package_id}")