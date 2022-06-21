import os

from waitress import serve
from app import create_app
from app.helpers.stepper import stepper
from env_loader import *
from config import Config

app = create_app(Config)

@stepper("serving")
def main():
  # serve(app, port=os.environ.get("PORT", 5000), host=os.environ.get("HOST"))
  app.run()

if __name__ == "__main__":
  main()