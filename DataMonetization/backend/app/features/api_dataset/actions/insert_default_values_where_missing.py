import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.helpers.action import action_response
from app.helpers.current_user import get_current_user

from app.helpers.http.response import report_not_found_error
from app.helpers.http.response import report_forbidden_error

from app.services.api_resource.get_by_id import get_api_resource_by_id
from app.services.api.get_by_id import get_api_by_id
from app.services.api_dataset.get_by_resource_id import get_dataset_by_resource_id

from app.services.api.should_own_api import should_own_api
from app.services.api_resource.should_belong_to_api import should_belong_to_api

from app.services.api_dataset.insert_default_values_where_missing import insert_default_values_where_missing as _insert_default_values_where_missing

route = router.routes["resolve missing data by inserting defaults"]

parameters = [
  {
    "name": "numeric",
    "type": "float",
    "default": 0.0
  },
  {
    "name": "nonnumeric",
    "type": "string",
    "default": "__MISSING_VALUE__"
  },
]

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, user_roles=route.roles, params={"src": "json", "defns": parameters})
def insert_default_values_where_missing(api_id, resource_id, numeric, nonnumeric, **kwargs):
  current_user = get_current_user()

  resource = get_api_resource_by_id(resource_id)
  api = get_api_by_id(api_id)

  should_belong_to_api(resource, api)
  should_own_api(current_user, api)

  dataset = get_dataset_by_resource_id(resource_id)
  dataset = _insert_default_values_where_missing(dataset)

  return action_response({"data": dataset.to_dict()})