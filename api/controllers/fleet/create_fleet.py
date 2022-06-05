import json
# import pytz

from flask import jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId
from datetime import datetime

from . import fleet_blueprint
from ...configurations.database import mongo

@fleet_blueprint.route("/create-fleet", methods=["POST"])
def create_fleet():
    fleet = request.json

    fleet_number = fleet["fleet_number"]
    fleet_capacity = int(fleet["fleet_capacity"])
    # allocation_status = fleet["allocation_status"]
    allocation_status = "FREE"
    # fleet_status = fleet["fleet_status"]
    fleet_status = "FREE"
    current_station = fleet["current_station"]
    creation_date = datetime.now()
    creation_date = creation_date.strftime("%Y-%m-%d %H:%M:%S")

    new_fleet_id = mongo.db.fleet.insert_one({
        "fleet_number": fleet_number,
        "fleet_capacity": fleet_capacity,
        "allocation_status": allocation_status,
        "fleet_status": fleet_status,
        "current_station": ObjectId(current_station),
        # "active_trip_origin": "NOT_SET",
        # "active_trip_target": "NOT_SET",
        "creation_date": creation_date,
        "record_status": "ACTIVE"
    }).inserted_id

    new_fleet = mongo.db.fleet.aggregate(
        [
            {"$match": {"$and": [{"_id": ObjectId(new_fleet_id)}, {"record_status": "ACTIVE"}]}},

            {"$lookup": {
                "from": "station",
                "foreignField": "_id",
                "localField": "current_station",
                "as": "current_station"
            }},

            {"$unwind": "$current_station"},
        ]
    )

    if new_fleet:
        new_fleet = json.loads(dumps(new_fleet))

        return jsonify({
            "status": "200",
            "message": "fleet_created_ok",
            "data": new_fleet
        })

    else:

        return jsonify({
            "status": "404",
            "message": "fleet_created_not_found",
            "data": []
        })