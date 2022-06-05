import json

from flask import jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId

from . import stations_blueprint
from ...configurations.database import mongo

@stations_blueprint.route("/connect-stations", methods=["POST"])
def connect_stations():
    stations = request.json
    stations = stations["stations"]

    new_stations_connection_id = mongo.db.connected_stations.insert_one({
        "stations": stations,
        "record_status": "ACTIVE",
    }).inserted_id

    new_stations_connection = mongo.db.connected_stations.find_one({
        "$and": [
            {"_id": ObjectId(new_stations_connection_id)},
            {"record_status": "ACTIVE"}
        ]
    })

    if new_stations_connection:
        new_stations_connection = json.loads(dumps(new_stations_connection))

        return jsonify({
            "status": "200",
            "message": "stations_connected_ok",
            "data": new_stations_connection
        })

    else:

        return jsonify({
            "status": "404",
            "message": "stations_connected_not_found",
            "data": []
        })

    # stations = mongo.db.station.find({
    #     "record_status": "ACTIVE",
    # })

    # if stations:
    #     stations = json.loads(dumps(stations))
    #     return jsonify({
    #         "status": "200",
    #         "message": "stations_retrieved_ok",
    #         "data": stations
    #     })

    # else:
    #     return jsonify({
    #         "status": "404",
    #         "message": "stations_not_found",
    #         "data": []
    #     })