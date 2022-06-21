import flask
import flask.helpers as flask_helpers

from flask_cors import CORS
from app.helpers.stepper import stepper

@stepper("configuring CORS")
def configure_cors(app):
  @app.before_request
  def hook():
    if flask.request.method == "OPTIONS":
      return flask_helpers.make_response("", 200)
    return None

  CORS(app, resources={r"/api/*": {"origins": "*"}})