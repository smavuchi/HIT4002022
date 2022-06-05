from flask import Flask, jsonify
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler

# Configurations
from ..configurations.database import mongo
from ..configurations.database import database_credentials
from ..configurations.auth import jwt
from ..configurations.auth import jwt_secret_key

# Blueprints
from ..controllers.auth import auth_blueprint
from ..controllers.waybill import waybill_blueprint
from ..controllers.stations import stations_blueprint
from ..controllers.fleet import fleet_blueprint
from ..controllers.conductor import conductor_blueprint
from ..controllers.users import user_blueprint
from ..controllers.possible_route import possible_route_blueprint
from ..controllers.routing import routing_blueprint
from ..controllers.live_feed import live_feed_blueprint

# Background Jobs
from ..native_functions.check_time_intervals import check_time_intervals

app = Flask(__name__)

CORS(app)

app.config["MONGO_URI"] = "mongodb://{}/{}".format(
    database_credentials["host"],
    database_credentials["database"]
)
mongo.init_app(app)

app.config["JWT_SECRET_KEY"] = jwt_secret_key
jwt.init_app(app)

def create_app():
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(waybill_blueprint)
    app.register_blueprint(stations_blueprint)
    app.register_blueprint(fleet_blueprint)
    app.register_blueprint(conductor_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(possible_route_blueprint)
    app.register_blueprint(routing_blueprint)
    app.register_blueprint(live_feed_blueprint)

    return app

# Predict Passengers Job
def run_prediction_job():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_time_intervals, "interval", seconds=5)
    scheduler.start()

# run_prediction_job()

app = create_app()