import os

from importlib import import_module
from .blueprint import blueprint

def init(app, feature):
  files = [x for x in os.listdir(f"app/features/{feature}/actions") if not x.startswith("__")]

  for file in files:
    import_module(f"app.features.{feature}.actions.{os.path.splitext(file)[0]}")

  app.register_blueprint(blueprint)