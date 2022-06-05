import json

from flask import jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId

from . import stations_blueprint
from ...configurations.database import mongo

# from ...native_functions.dijkstra.dijkstra import dijkstra

@stations_blueprint.route("/shortest-path", methods=["GET"])
def shortest_path():
    # Fetch all stations
    stations = mongo.db.station.find({
        "record_status": "ACTIVE",
    })
    stations = json.loads(dumps(stations))

    # Fetch all connected stations
    connected_stations = mongo.db.connected_stations.find({
        "record_status": "ACTIVE",
    })
    connected_stations = json.loads(dumps(connected_stations))

    print("STATIONS", stations)
    print("CONNECTED STATIONS", connected_stations)

    # dijkstra(stations, connected_stations)
    
    return jsonify({
        "text": "shortest path"
    })