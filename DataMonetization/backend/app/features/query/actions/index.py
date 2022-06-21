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

from app.services.api.get_by_name import get_api_by_name
from app.services.api_resource.get_by_name import get_resource_by_name
from app.services.api.should_be_published import should_be_published as api_should_be_published
from app.services.api_resource.should_be_published import should_be_published as resource_should_be_published
from app.services.api_query.index import index_api_resource as _index_api_resource
from app.services.api_query.save_request_data import save_request_data

route = router.routes["perform a GET query on an API endpoint"]
route.set_parameters(parameters)

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, params={"src": "query", "defns": parameters}, user_roles=route.roles)
def index_api_resource(offset, limit, api_name, resource_name, columns, **kwargs):
  current_user = get_current_user()

  api = get_api_by_name(api_name)
  resource = get_resource_by_name(resource_name)

  if "index" not in resource.actions:
    report_forbidden_error("resource action not allowed")

  api_should_be_published(api)
  resource_should_be_published(resource)
  save_request_data(current_user, api)

  columns = [x.strip() for x in columns.split(",")] if columns else []

  data = _index_api_resource(resource, offset=offset, limit=limit, columns=columns)
  return action_response({"data": data})