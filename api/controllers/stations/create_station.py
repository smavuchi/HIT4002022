import json
from turtle import update

from flask import jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId

from . import stations_blueprint
from ...configurations.database import mongo

@stations_blueprint.route("/create-station", methods=["POST"])
def create_station():
    station = request.json

    station_name = station["station_name"]

    new_station_id = mongo.db.station.insert_one({
        "station_name": station_name,
        "last_pickup_time": "NOT SET",
        "last_pickup_fleet": "NOT SET",
        "record_status": "ACTIVE"
    }).inserted_id

    new_station = mongo.db.station.find_one({
        "$and": [
            {"_id": ObjectId(new_station_id)},
            {"record_status": "ACTIVE"}
        ]
    })

    if new_station:
        new_station = json.loads(dumps(new_station))

        return jsonify({
            "status": "200",
            "message": "station_created_ok",
            "data": new_station
        })

    else:

        return jsonify({
            "status": "404",
            "message": "station_created_not_found",
            "data": []
        })