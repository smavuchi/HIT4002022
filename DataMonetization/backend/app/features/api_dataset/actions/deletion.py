import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.helpers.action import action_response
from app.helpers.current_user import get_current_user

from app.helpers.http.response import report_not_found_error
from app.helpers.http.response import report_forbidden_error

from app.services.api_resource.get_by_id import get_api_resource_by_id
from app.services.api_dataset.delete_api_dataset import delete_api_dataset as _delete_api_dataset
from app.services.api.get_by_id import get_api_by_id

from app.services.api_resource.should_belong_to_api import should_belong_to_api
from app.services.api.should_own_api import should_own_api

route = router.routes["delete an api dataset"]

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, user_roles=route.roles)
def delete_api_dataset(api_id, resource_id, **kwargs):
  current_user = get_current_user()

  api = get_api_by_id(api_id)
  resource = get_api_resource_by_id(resource_id)

  should_belong_to_api(resource, api)
  should_own_api(current_user, api)

  _delete_api_dataset(resource_id)
  return action_response()