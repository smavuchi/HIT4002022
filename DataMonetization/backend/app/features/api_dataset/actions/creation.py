import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.services.api_dataset.create import create_dataset
from app.helpers.action import action_response
from app.helpers.current_user import get_current_user

from app.services.api.get_by_id import get_api_by_id
from app.services.api_resource.get_by_id import get_api_resource_by_id

from app.services.api_resource.should_belong_to_api import should_belong_to_api
from app.services.api.should_own_api import should_own_api

from .__creation_params import parameters

route = router.routes["add a dataset"]
route.set_parameters(parameters)

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, params={"src": "form-data", "defns": parameters}, user_roles=route.roles)
def create_api_dataset(api_id, resource_id, **kwargs):
  current_user = get_current_user()

  api = get_api_by_id(api_id)
  resource = get_api_resource_by_id(resource_id)

  should_belong_to_api(resource, api)
  should_own_api(current_user, api)

  result = create_dataset(resource_id=str(resource.id), **kwargs)
  return action_response({"data": result.to_dict()})