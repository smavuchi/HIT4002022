import flask

from werkzeug.exceptions import BadRequest
from werkzeug.exceptions import InternalServerError
from werkzeug.exceptions import NotFound
from werkzeug.exceptions import ServiceUnavailable
from werkzeug.exceptions import Unauthorized
from werkzeug.exceptions import Forbidden
from werkzeug.exceptions import NotImplemented
from werkzeug.exceptions import UnprocessableEntity

def make_response(data=None, status=200, message=None, headers={}, **kwargs):
  response = flask.make_response(flask.jsonify({
    "data": data,
    "status": status,
    "message": message,
    "success": status < 400,
    **kwargs
  }), 200)

  for key in headers:
    response.headers[key] = headers[key]

  return response

def report_bad_request_error(message="invalid information provided"):
  raise BadRequest(message)

def report_internal_server_error(message="an internal server error occured"):
  raise InternalServerError(message)

def report_not_found_error(message="resource not found"):
  raise NotFound(message)

def report_unauthorized_error(message="unauthorized"):
  raise Unauthorized(message)

def report_forbidden_error(message="forbidden"):
  raise Forbidden(message)

def report_unimplemented_error(message="unimplemented"):
  raise NotImplemented(message)

def report_account_verification_error(message="account needs to be verified"):
  raise Unauthorized(message)

def report_expired_token_error(message="token expired"):
  raise Unauthorized(message)

def report_invalid_token_error(message="invalid token provided"):
  raise UnprocessableEntity(message)

def report_expired_api_key_error(message="api key expired"):
  raise Unauthorized(message)

def report_invalid_api_key_error(message="invalid api key provided"):
  raise UnprocessableEntity(message)