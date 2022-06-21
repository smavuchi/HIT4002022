import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.services.api_dataset.create import create_dataset
from app.helpers.action import action_response
from app.helpers.current_user import get_current_user
from app.helpers.http.response import report_bad_request_error

from app.services.api.get_by_id import get_api_by_id
from app.services.api_resource.get_by_id import get_api_resource_by_id
from app.services.api_dataset.get_by_resource_id import get_dataset_by_resource_id

from app.services.api_resource.should_belong_to_api import should_belong_to_api
from app.services.api.should_own_api import should_own_api
from app.services.api_dataset.set_column_types import set_column_types

from .__set_column_types_params import parameters

route = router.routes["set column types"]
route.set_parameters(parameters)

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, params={"src": "json", "defns": parameters}, user_roles=route.roles)
def set_dataset_column_types(api_id, resource_id, column_types, **kwargs):
  current_user = get_current_user()

  api = get_api_by_id(api_id)
  resource = get_api_resource_by_id(resource_id)

  should_belong_to_api(resource, api)
  should_own_api(current_user, api)
  
  dataset = get_dataset_by_resource_id(resource_id)

  try:
    dataset = set_column_types(dataset, column_types)
  except:
    report_bad_request_error("type conversion failed. Ensure that no missing values are in the dataset")

  return action_response({"data": dataset.to_dict()})