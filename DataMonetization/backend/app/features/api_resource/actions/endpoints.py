import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.helpers.middleware import middleware
from app.helpers.action import action_response
from app.helpers.current_user import get_current_user

from app.helpers.http.response import report_not_found_error
from app.helpers.http.response import report_forbidden_error

from app.services.api_resource.get_by_id import get_api_resource_by_id
from app.services.api_resource.should_belong_to_api import should_belong_to_api
from app.services.api.get_by_id import get_api_by_id
from app.services.api.should_own_api import should_own_api

from app.services.api_dataset.get_by_resource_id import get_dataset_by_resource_id

route = router.routes["get API endpoints"]

@blueprint.route(route.url, methods=route.methods)
@middleware(*route.middleware, user_roles=route.roles)
def get_api_endpoints(api_id, resource_id, **kwargs):
  current_user = get_current_user()

  resource = get_api_resource_by_id(resource_id)
  api = get_api_by_id(api_id)

  should_belong_to_api(resource, api)
  should_own_api(current_user, api)

  dataset = get_dataset_by_resource_id(resource_id, throw=False)
  parameters = [x for x in dataset.column_types] if dataset else []

  endpoints = []

  if "create" in resource.actions:
    endpoints.append({
      "url": f"/api/v1/query/{api.name}/{resource.url_name}",
      "methods": ["POST"],
      "parameters": parameters,
      "description": f"creates a new resource ({resource.name})"
      })
  
  if "index" in resource.actions:
    endpoints.append({
      "url": f"/api/v1/query/{api.name}/{resource.url_name}",
      "methods": ["GET"],
      "parameters": [],
      "description": f"retrieve all resources ({resource.name})"
      })
  
  if "show" in resource.actions:
    endpoints.append({
      "url": f"/api/v1/query/{api.name}/{resource.url_name}/<string:id>",
      "methods": ["GET"],
      "parameters": [],
      "description": f"retrieves the specified resource ({resource.name})"
      })
  
  if "delete" in resource.actions:
    endpoints.append({
      "url": f"/api/v1/query/{api.name}/{resource.url_name}/<string:id>",
      "methods": ["DELETE"],
      "parameters": [],
      "description": f"deletes the specified resource ({resource.name})"
      })
  
  if "clear" in resource.actions:
    endpoints.append({
      "url": f"/api/v1/query/{api.name}/{resource.url_name}",
      "methods": ["DELETE"],
      "parameters": [],
      "description": f"clears all resources ({resource.name})"
      })
  
  if "update" in resource.actions:
    endpoints.append({
      "url": f"/api/v1/query/{api.name}/{resource.url_name}/<string:id>",
      "methods": ["PUT", "PATCH"],
      "parameters": parameters,
      "description": f"updates the given resource ({resource.name})"
      })

  return action_response({"data": endpoints})