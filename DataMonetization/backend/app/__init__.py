import flask
import os

from importlib import import_module

from .configure import configure
from .routes import create_routes
from .middleware import create_middleware
from .helpers.stepper import stepper
from .helpers.router import router

@stepper("creating raw flask app")
def create_flask_app(config):
  app = flask.Flask(__name__)
  app.config.from_object(config)
  return app

@stepper("creating features")
def create_features(app):
  feature_names = [f for f in next(os.walk(f"app/features"))[1] if not f.startswith("__")]

  for feature_name in feature_names:
    feature = import_module('app.features.%s' % feature_name)
    feature.init(app, feature_name)

@stepper("resolving routes - ensuring no conflicts")
def resolve_routes():
  resolved, data = router.resolve()
  return data

@stepper("configuring routes")
def configure_routes(app):
  create_routes()
  resolve_routes()

@stepper("creating app")
def create_app(config):
  app = create_flask_app(config)
  configure(app)
  create_middleware(app)
  configure_routes(app)
  create_features(app)
  return app