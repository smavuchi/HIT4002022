import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.helpers.action import action_response
from app.helpers.current_user import get_current_user

from app.helpers.database.mongo import str_to_id

from app.helpers.http.response import report_not_found_error
from app.helpers.http.response import report_forbidden_error

from app.services.api.get_by_id import get_api_by_id
from app.helpers.time import get_current_time
from app.models.api_subscription import APISubscription

from .__index_params import parameters

route = router.routes["get API packages"]
route.set_parameters(parameters)

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, params={"src": "query", "defns": parameters}, user_roles=route.roles)
def index_packages(api_id, offset, limit, **kwargs):
  api = get_api_by_id(api_id)
  current_user = get_current_user()

  if api.owner.id != current_user.id:
    report_forbidden_error()

  packages = [x.to_dict() for x in api.packages]

  for package in packages:
    if APISubscription.objects(
      api_id=api_id, 
      user_id=str(current_user.id), 
      package_id=package["id"],
      expires_at__gt=get_current_time()
      ).first():
      package["subscribed"] = True
    else:
      package["subscribed"] = False

  return action_response({"data": packages[offset:limit]})