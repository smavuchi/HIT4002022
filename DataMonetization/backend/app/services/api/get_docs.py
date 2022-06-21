from app.models.api_endpoint_param import APIEndpointParam

def get_api_docs(api):
  result = {}

  for endpoint in api.endpoints:
    result[endpoint.url] = endpoint.to_dict()

  return result