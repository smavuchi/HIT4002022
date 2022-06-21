import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.helpers.action import action_response
from app.helpers.current_user import get_current_user

from app.services.api.get_by_id import get_api_by_id
from app.services.api_package.subscribe import subscribe_to_api_package as _subscribe_to_api_package

from app.helpers.http.response import report_not_found_error

route = router.routes["make an API subscription"]

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, params={"src": "json"}, user_roles=route.roles)
def subscribe_to_api_package(api_id, package_id, **kwargs):
  current_user = get_current_user()
  api = get_api_by_id(api_id)

  for package in api.packages:
    if str(package.id) == package_id:
      result = _subscribe_to_api_package(api=api, package=package, user=current_user)
      return action_response({"data": result.to_dict()})

  report_not_found_error(f"package not found: {package_id}")