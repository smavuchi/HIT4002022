import json

from flask import jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId

from . import waybill_blueprint
from ...configurations.database import mongo

@waybill_blueprint.route("/update-trip", methods=["PUT"])
def update_trip():
    trip = request.json

    trip_id = trip["trip_id"]
    # trip_id = trip_id["$oid"]
    fleet_number = trip["fleet_number"]
    departure_time = trip["departure_time"]
    arrival_time =  trip["arrival_time"]
    pickup_station =  trip["pickup_station"]
    dropoff_station =  trip["dropoff_station"]
    head_count =  trip["head_count"]
    surplus_count =  trip["surplus_count"]
    trip_status = trip["trip_status"]

    mongo.db.trip.update_one({
            "_id": ObjectId(trip_id),
        },

        {"$set": {
            "fleet_number": fleet_number,
            "departure_time": departure_time,
            "arrival_time": arrival_time,
            "pickup_station": pickup_station,
            "dropoff_station": dropoff_station,
            "head_count": head_count,
            "surplus_count": surplus_count,
            "trip_status": trip_status,
        }
    })

    updated_trip = mongo.db.trip.find_one({
        "$and": [
            {"_id": ObjectId(trip_id)},
            {"record_status": "ACTIVE"}
        ]
    })

    if updated_trip:
        updated_trip = json.loads(dumps(updated_trip))

        return jsonify({
            "status": "200",
            "message": "trip_updated_ok",
            "data": updated_trip
        })

    else:
        return jsonify({
            "status": "404",
            "message": "trip_not_found",
            "data": []
        })