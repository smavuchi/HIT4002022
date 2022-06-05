import json
import pickle
import numpy as np
from datetime import datetime

from flask import jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId

from . import possible_route_blueprint
from ...configurations.database import mongo
from ...native_functions.predict_passengers import predict_route_passengers
from ...native_functions.routing_engine.get_stations import get_stations
from ...native_functions.routing_engine.get_station_predictions import get_station_predictions
from ...native_functions.routing_engine.get_connected_stations import get_connected_stations
from ...native_functions.routing_engine.dijkstra import dijkstra

@possible_route_blueprint.route("/get-optimal-route", methods=["POST"])
def get_optimal_route():
    prediction_input = request.json
    current_station = prediction_input["current_station"]
    include_last_pickup_time = prediction_input["include_last_pickup_time"]

    print("***FILTERING PARAMS***")
    print(include_last_pickup_time)

    stations = get_stations()

    connected_stations = get_connected_stations()

    connected_stations = get_station_predictions(stations, connected_stations)

    optimal_route = dijkstra(stations, connected_stations, current_station)
    optimal_route.reverse()

    print("ALL STATIONS WITH PREDICTIONS")
    print(stations)

    print("CONNECTED STATIONS")
    print(connected_stations)

    print("OPTIMAL ROUTE")
    print(optimal_route)
    # print(optimal_route.reverse())

    # current_station = prediction_input["current_station"]

    return jsonify({
        "status": "200",
        "message": "optimal_route_retrieved_ok",
        "data": optimal_route,
    })