import json
import random
import statistics

from bson.json_util import dumps
from bson.objectid import ObjectId

from ...configurations.database import mongo
from .run_prediction_model import run_prediction_model

def get_station_predictions(stations, connected_stations):
    # fleet_capacity = int(prediction_input["fleet_capacity"])
    # possible_routes_predictions = []

    station_names = [
        "Marlborough",
        "Mount Pleasant",
        "Mabelreign",
        "Belvedere",
        "Westgate",
        "Warren Park",
        "Kuwadzana",
        "City",
        "Dzivarasekwa",
        "Vainona"
    ]

    for station in stations:
        predictions = []
        
        station_name = station["station_name"]
        station_id = station["_id"]["$oid"]

        if station_name in station_names:
            prediction_count = run_prediction_model(station_name)
            station["prediction_count"] = prediction_count

            for connection in connected_stations:
                if station_id in connection["stations"]:
                    connection["stations"][2].append(prediction_count)
            # prediction_count = random.randint(0, 10)

            station["prediction_count"] = prediction_count

    for connection in connected_stations:
        average = statistics.mean(connection["stations"][2])
        # average = -abs(average)
        # average = (-1) * (average)
        # print(type(average))
        connection["stations"].append(average)
    
    return connected_stations