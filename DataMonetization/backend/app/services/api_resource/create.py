import flask
from app.models.api_resource import APIResource
from app.helpers.models import Model

from app.helpers.http.response import report_bad_request_error
from app.helpers.http.response import report_internal_server_error
from app.helpers.http.response import report_forbidden_error

def make_url_friendly(text):
  if not text:
    return text
  
  text = text.lower()

  while "  " in text:
    text = text.replace("  ", " ")

  return text.replace(" ", "-")

def create_api_resource(api, url_prefix, url_name, **attributes):
  url_name = make_url_friendly(url_name if url_name else attributes.get("name"))
  url_prefix = make_url_friendly(url_prefix) if url_prefix else ""

  if APIResource.objects(name=attributes.get("name"), api_id=str(api.id)).first():
    report_forbidden_error("name already taken")

  if APIResource.objects(url_name=url_name, api_id=api.id).first():
    report_forbidden_error("url_name already taken by another resource. Will cause ambiguity")

  created, resource = Model.create(APIResource, 
    api_id=str(api.id), 
    url_prefix=url_prefix,
    url_name=url_name,
    **attributes)

  if not created:
    report_bad_request_error(resource)

  modified, result = Model.modify(api, add_to_set__resources=resource)

  if not modified:
    report_internal_server_error(result)

  return resource