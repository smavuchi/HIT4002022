import json
import random
import statistics
import copy

from bson.json_util import dumps
from bson.objectid import ObjectId

from ...configurations.database import mongo
from .run_prediction_model import run_prediction_model

def get_station_statuses(stations, prediction_day, prediction_time):
    # fleet_capacity = int(prediction_input["fleet_capacity"])
    # possible_routes_predictions = []

    depart_trip_stations = copy.deepcopy(stations)
    return_trip_stations = copy.deepcopy(stations)

    station_names = [
        "Marlborough",
        "Mount Pleasant",
        "Mabelreign",
        "Belvedere",
        "Westgate",
        "Warren Park",
        "Kuwadzana",
        # "City",
        "Dzivarasekwa",
        "Vainona"
    ]

    for station in return_trip_stations:
        predictions = []
        
        station_name = station["station_name"]
        station_id = station["_id"]["$oid"]

        if station_name in station_names:
            # prediction_count = run_prediction_model(station_name)
            prediction = run_prediction_model(prediction_day=prediction_day, prediction_time=prediction_time, pickup_station=station_name, dropoff_station="City")
            prediction_count = prediction["prediction_count"]
            pickup_station = prediction["pickup_station"]
            dropoff_station = prediction["dropoff_station"]
            
            station["pickup_station"] = pickup_station
            station["dropoff_station"] = dropoff_station
            station["prediction_count"] = prediction_count

            # station["prediction_count"] = prediction_count

    for station in depart_trip_stations:
        predictions = []
        
        station_name = station["station_name"]
        station_id = station["_id"]["$oid"]

        if station_name in station_names:
            # prediction_count = run_prediction_model(station_name)
            prediction = run_prediction_model(prediction_day=prediction_day, prediction_time=prediction_time, pickup_station="City", dropoff_station=station_name)
            prediction_count = prediction["prediction_count"]
            pickup_station = prediction["pickup_station"]
            dropoff_station = prediction["dropoff_station"]
            
            station["pickup_station"] = pickup_station
            station["dropoff_station"] = dropoff_station
            station["prediction_count"] = prediction_count

    # print(depart_trip_stations)
    # print("----")
    # print(return_trip_stations)

    stations = depart_trip_stations + return_trip_stations
    stations = [x for x in stations if not (x["station_name"] == "Depot" or x["station_name"] == "City")]
    
    return stations