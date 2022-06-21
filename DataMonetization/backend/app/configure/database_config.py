from mongoengine import connect
from app.helpers.stepper import stepper

@stepper("connecting to database")
def connect_to_database(app):
  connect(host=app.config["MONGO_CONNECTION_STRING"])

@stepper("configuring database")
def configure_database(app):
  connect_to_database(app)