from .cors_config import configure_cors
from .database_config import configure_database
from .error_config import configure_errors

from app.helpers.stepper import stepper

@stepper("configuring")
def configure(app):
  configure_cors(app)
  configure_database(app)
  configure_errors(app)
  return app