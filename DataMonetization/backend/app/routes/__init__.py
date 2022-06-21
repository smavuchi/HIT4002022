import os

from importlib import import_module
from app.helpers.stepper import stepper

@stepper("creating routes")
def create_routes():
  files = os.listdir("app/routes")

  for file in files:
    if file.startswith("__") and file.endswith("__"):
      continue

    if os.path.isdir(file):
      pass
    else:
      module = import_module(f".{os.path.splitext(file)[0]}", "app.routes")