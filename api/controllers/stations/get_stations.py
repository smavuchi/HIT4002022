import json

from flask import jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId

from . import stations_blueprint
from ...configurations.database import mongo

@stations_blueprint.route("/get-stations")
def get_stations():
    stations = mongo.db.station.find({
        "record_status": "ACTIVE",
    })

    if stations:
        stations = json.loads(dumps(stations))
        return jsonify({
            "status": "200",
            "message": "stations_retrieved_ok",
            "data": stations
        })

    else:
        return jsonify({
            "status": "404",
            "message": "stations_not_found",
            "data": []
        })