import os

from importlib import import_module
from app.helpers.stepper import stepper
from app.helpers.middleware import register_middleware

@stepper("creating middleware")
def create_middleware(app):
  files = [x for x in os.listdir(f"app/middleware") if not x.startswith("__")]

  for file in files:
    module = import_module(f"app.middleware.{os.path.splitext(file)[0]}")
    register_middleware(os.path.splitext(file)[0], module.middleware)