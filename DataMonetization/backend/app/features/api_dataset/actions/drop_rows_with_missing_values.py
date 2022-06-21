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

from app.services.api_dataset.drop_rows_with_missing_values import drop_rows_with_missing_values as _drop_rows_with_missing_values

route = router.routes["resolve missing data by dropping rows"]

parameters = [
  {
    "name": "min",
    "type": "float"
  },
  # {
  #   "name": "max",
  #   "type": "float"
  # },
]

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, user_roles=route.roles, params={"src": "json", "defns": parameters})
def drop_rows_with_missing_values(api_id, resource_id, min, **kwargs):
  current_user = get_current_user()

  resource = get_api_resource_by_id(resource_id)
  api = get_api_by_id(api_id)

  should_belong_to_api(resource, api)
  should_own_api(current_user, api)

  dataset = get_dataset_by_resource_id(resource_id)
  dataset = _drop_rows_with_missing_values(dataset, _min=min)

  return action_response({"data": dataset.to_dict()})