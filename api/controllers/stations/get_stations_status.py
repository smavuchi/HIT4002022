import json

from flask import jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId

from . import stations_blueprint
from ...configurations.database import mongo
from ...native_functions.routing_engine.get_station_statuses import get_station_statuses

@stations_blueprint.route("/get-stations-status", methods=["POST"])
def get_stations_status():
    prediction_body = request.json
    # print(prediction_body)
    prediction_day = prediction_body["prediction_day"]
    prediction_time = prediction_body["prediction_time"]

    stations = mongo.db.station.find({
        "record_status": "ACTIVE",
    })

    if stations:
        stations = json.loads(dumps(stations))

        stations = get_station_statuses(stations, prediction_day, prediction_time)

        return jsonify({
            "status": "200",
            "message": "stations_status_retrieved_ok",
            "data": stations
        })

    else:
        return jsonify({
            "status": "404",
            "message": "stations_status_not_found",
            "data": []
        })