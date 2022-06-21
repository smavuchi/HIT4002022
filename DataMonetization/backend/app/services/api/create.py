import flask
from app.models.api import API

from app.helpers.http.response import report_bad_request_error
from app.helpers.http.response import report_forbidden_error
from app.helpers.models import Model

def create_api(**attributes):
  if API.objects(name=attributes.get("name")).first():
    report_forbidden_error("name already taken")

  created, result = Model.create(API, **attributes)

  if not created:
    report_bad_request_error(result)

  return result