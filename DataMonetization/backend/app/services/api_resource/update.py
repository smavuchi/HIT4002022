from app.models.api_resource import APIResource

from app.helpers.http.response import report_bad_request_error
from app.helpers.http.response import report_forbidden_error

from app.helpers.models import Model

def make_url_friendly(text):
  if not text:
    return text
  
  text = text.lower()

  while "  " in text:
    text = text.replace("  ", " ")

  return text.replace(" ", "-")

def update_api_resource(resource, url_name, url_prefix, actions, **attributes):
  url_name = make_url_friendly(url_name if url_name else attributes.get("name"))
  url_prefix = make_url_friendly(url_prefix) if url_prefix else ""

  if APIResource.objects(name=attributes.get("name"), api_id=str(resource.api_id)).first() and resource.name != attributes.get("name"):
    report_forbidden_error("name already taken")

  if APIResource.objects(url_name=url_name, api_id=resource.api_id).first() and resource.url_name != url_name:
    report_forbidden_error("url_name already taken by another resource. Will cause ambiguity")

  new_actions = resource.actions

  if actions is not None:
    new_actions = actions

  modified, result = Model.modify(resource, 
    url_name=url_name,
    url_prefix=url_prefix,
    actions=new_actions,
    **attributes)

  if not modified:
    report_bad_request_error(result)

  return result