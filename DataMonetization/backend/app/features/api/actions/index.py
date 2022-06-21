import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.helpers.action import action_response
from app.helpers.current_user import get_current_user

from app.helpers.database.mongo import str_to_id

from app.helpers.http.response import report_not_found_error
from app.helpers.http.response import report_forbidden_error

from app.services.api.get_all import get_all_apis

from .__index_params import parameters

route = router.routes["get apis"]
route.set_parameters(parameters)

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, params={"src": "query", "defns": parameters}, user_roles=route.roles)
def index_apis(offset, limit, owner, **kwargs):
  apis = [x.to_dict() for x in get_all_apis(owner=owner, limit=limit, offset=offset)]
  current_user = get_current_user()
  to_delete = []

  for api in apis:
    if not api["published"]:
      if str_to_id(api["owner"]["id"]) != current_user.id:
        to_delete.append(api["id"])

  result = list(filter(lambda x: x["id"] not in to_delete, apis))
  return action_response({"data": result})

@blueprint.route(route.url + "/mine", methods=route.methods)
@middleware(*route.middleware, params={"src": "query", "defns": parameters}, user_roles=route.roles)
def index_my_apis(offset, limit, owner, **kwargs):
  current_user = get_current_user()
  to_delete = []

  apis = [x.to_dict() for x in get_all_apis(owner=current_user.email, limit=limit, offset=offset)]

  for api in apis:
    if not api["published"]:
      if str_to_id(api["owner"]["id"]) != current_user.id:
        to_delete.append(api["id"])

  result = list(filter(lambda x: x["id"] not in to_delete, apis))
  return action_response({"data": result})