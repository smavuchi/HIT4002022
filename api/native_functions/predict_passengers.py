import json
import random

from bson.json_util import dumps
from bson.objectid import ObjectId

from ..configurations.database import mongo
from .station_prediction import station_prediction

def predict_route_passengers(possible_routes, prediction_input):
    fleet_capacity = int(prediction_input["fleet_capacity"])
    possible_routes_predictions = []
    print("***")

    for route in possible_routes:
        predictions = []
        for station_id in route["route"]:
            # FETCH ACTUAL STATION
            station = mongo.db.station.find_one({
                "_id": ObjectId(station_id['$oid'])
            })

            if station:
                station = json.loads(dumps(station))

            station_name = station["station_name"]

            prediction_count = station_prediction(prediction_input, station_name)
            # prediction_count = random.randint(0, 10)
            
            prediction = {
                "station": station_id["$oid"],
                "prediction_count": prediction_count,
            }

            predictions.append(prediction)
    
        route_passengers_total = sum(x.get("prediction_count", 0) for x in predictions)

        possible_routes_predictions.append({
            "route_id": route["_id"]["$oid"],
            "predictions": predictions,
            "route_passengers_total": route_passengers_total,
            "fleet_capacity": fleet_capacity,
        })

        print("***{}***".format(possible_routes_predictions))
    
    appropriate_route = min(possible_routes_predictions, key=lambda x:abs(x["route_passengers_total"] - fleet_capacity), default="NOT ROUTE")

    predictions = {
        # "possible_routes_predictions": possible_routes_predictions,
        "appropriate_route": appropriate_route,
        "possible_routes": possible_routes_predictions,
    }

    return predictions

def predict_passengers(station):
    prediction_count = random.randint(0, 10)
    prediction = {
        "station_name": station["station_name"],
        "prediction_count": prediction_count
    }
    return prediction