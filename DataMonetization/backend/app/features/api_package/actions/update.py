import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.helpers.action import action_response
from app.helpers.current_user import get_current_user

from app.services.api.get_by_id import get_api_by_id
from app.services.api_package.update import update_api_package as _update_api_package

from app.services.api_resource.should_belong_to_api import should_belong_to_api
from app.services.api.should_own_api import should_own_api

from app.helpers.http.response import report_not_found_error

from .__update_params import parameters

route = router.routes["update an API package"]
route.set_parameters(parameters)

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, params={"src": "json", "defns": parameters}, user_roles=route.roles)
def update_api_package(api_id, package_id, **kwargs):
  current_user = get_current_user()
  api = get_api_by_id(api_id)
  should_own_api(current_user, api)

  for package in api.packages:
    if str(package.id) == package_id:
      result = _update_api_package(package, **kwargs)
      return action_response({"data": result.to_dict()})

  report_not_found_error(f"package not found: {package_id}")