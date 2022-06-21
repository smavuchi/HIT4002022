import flask
import datetime

from app.helpers.token import decode_token
from app.helpers.time import get_current_time
from app.helpers.http.response import report_expired_api_key_error
from app.helpers.http.response import report_invalid_api_key_error
from app.helpers.http.response import report_invalid_token_error
from app.helpers.http.response import report_forbidden_error
from app.services.user.find_by_id import find_user_by_id
from app.services.user.find_by_api_key import find_user_by_api_key

def authorize_api_key(key):
  user = find_user_by_api_key(key)

  if not user:
    report_invalid_api_key_error()

  if user.api_key_expires_at < get_current_time():
    report_expired_api_key_error()

  flask.g.user = user

def authorize_token(token):
  info = decode_token(token)
  user = find_user_by_id(info["id"])

  if not user:
    report_invalid_token_error("token invalid: no such user exists")

  flask.g.user = user

def authorize_user_roles(roles):
  if len(roles) == 0:
    return
  
  if flask.g.user.role not in roles:
    report_forbidden_error()

def middleware(user_roles=[], **kwargs):
  if "api-key" in flask.request.args:
    authorize_api_key(flask.request.args["api-key"])

  elif "token" in flask.request.headers:
    authorize_token(flask.request.headers["token"])

  elif "authorization" in flask.request.headers:
    value = flask.request.headers["authorization"]
    if value.startswith("Bearer"):
      value = value[len("Bearer")+1:]
    authorize_token(value)

  elif "api-key" in flask.request.form:
    authorize_api_key(flask.request.form["api-key"])

  elif flask.request.json and "api-key" in flask.request.json:
    authorize_api_key(flask.request.json["api-key"])

  else:
    flask.g.user = None

  authorize_user_roles(user_roles)