from app.helpers.models import Model
from app.models.api_request import APIRequest

from app.services.api_resource.delete_api_resource import delete_api_resource
from app.services.api_package.delete_api_package import delete_api_package

def delete_api(api):
  # resources
  for resource in api.resources:
    delete_api_resource(api, resource)

  for package in api.packages:
    delete_api_package(api, package)

  for request in APIRequest.objects(api_id=str(api.id)):
    request.delete()

  api.delete()