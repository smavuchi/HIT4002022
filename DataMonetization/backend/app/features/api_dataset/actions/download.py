import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.helpers.current_user import get_current_user
from app.helpers.files import download_file

from app.services.api_resource.get_by_id import get_api_resource_by_id
from app.services.api.get_by_id import get_api_by_id
from app.services.api_dataset.get_by_resource_id import get_dataset_by_resource_id

from app.services.api.should_own_api import should_own_api
from app.services.api_resource.should_belong_to_api import should_belong_to_api

route = router.routes["download a dataset"]

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, user_roles=route.roles, params={"src": "query"})
def download_api_dataset(api_id, resource_id, **kwargs):
  current_user = get_current_user()

  resource = get_api_resource_by_id(resource_id)
  api = get_api_by_id(api_id)

  should_belong_to_api(resource, api)
  should_own_api(current_user, api)

  dataset = get_dataset_by_resource_id(resource_id)
  return download_file(dataset.filename)