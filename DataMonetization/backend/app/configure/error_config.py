from werkzeug.exceptions import BadRequest
from werkzeug.exceptions import InternalServerError
from werkzeug.exceptions import MethodNotAllowed
from werkzeug.exceptions import NotFound
from werkzeug.exceptions import ServiceUnavailable
from werkzeug.exceptions import Unauthorized

from werkzeug.exceptions import Forbidden
from werkzeug.exceptions import NotImplemented
from werkzeug.exceptions import RequestEntityTooLarge
from werkzeug.exceptions import RequestHeaderFieldsTooLarge
from werkzeug.exceptions import RequestURITooLarge
from werkzeug.exceptions import TooManyRequests
from werkzeug.exceptions import UnprocessableEntity
from werkzeug.exceptions import Unauthorized

from app.helpers.http.response import make_response
from app.helpers.stepper import stepper

@stepper("configuring error handlers")
def configure_errors(app):
  errors = [
    BadRequest, 
    InternalServerError, 
    MethodNotAllowed, 
    NotFound, 
    ServiceUnavailable,
    Forbidden,
    NotImplemented,
    RequestEntityTooLarge,
    RequestURITooLarge,
    RequestHeaderFieldsTooLarge,
    TooManyRequests,
    UnprocessableEntity,
    Unauthorized
  ]

  for exception in errors:
    @app.errorhandler(exception)
    def handle_exception(e):
      status = int(e.code)
      return make_response(message=e.description, status=status)