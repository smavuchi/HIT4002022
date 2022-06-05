import json
import traceback

from flask import jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId
from datetime import datetime

from . import fleet_blueprint
from ...configurations.database import mongo

@fleet_blueprint.route("/allocate-fleet", methods=["PUT"])
def allocate_fleet():
    fleet = request.json

    conductor_id = fleet["conductor_id"]
    fleet_id = fleet["fleet_id"]
    allocation_date = datetime.now()
    allocation_date = allocation_date.strftime("%Y-%m-%d %H:%M:%S")

    try:
        mongo.db.user.update_one({
                "_id": ObjectId(conductor_id),
            },

            {"$set": {
                "allocation_status": "ALLOCATED",
                "allocated_fleet": fleet_id,
            }
        })

        try:
            mongo.db.fleet.update_one({
                    "_id": ObjectId(fleet_id),
                },

                {"$set": {
                    "allocation_status": "ALLOCATED",
                    "allocated_conductor": conductor_id,
                }
            })

            # allocated_fleet = mongo.db.fleet.find_one({
            #     "$and": [
            #         {"_id": ObjectId(fleet_id)},
            #         {"record_status": "ACTIVE"}
            #     ]
            # })

            allocated_fleet = mongo.db.fleet.aggregate(
                [
                    {"$match": {"$and": [{"_id": ObjectId(fleet_id)}, {"record_status": "ACTIVE"}]}},

                    # THERE IS NEED TO FILTER OUT 'PASSWORD', WILL BE BACK IN THE FUTURE...

                    {"$lookup": {
                        "from": "station",
                        "foreignField": "_id",
                        "localField": "current_station",
                        "as": "current_station"
                    }},

                    {"$unwind": "$current_station"},
                ]
            )

            try:
                new_fleet_allocation_id = mongo.db.fleet_allocation.insert_one({
                    "conductor_id": conductor_id,
                    "fleet_id": fleet_id,
                    "allocation_date": allocation_date,
                    "record_status": "ACTIVE"
                }).inserted_id

                new_fleet_allocation = mongo.db.fleet_allocation.find_one({
                    "$and": [
                        {"_id": ObjectId(new_fleet_allocation_id)},
                        {"record_status": "ACTIVE"}
                    ]
                })

                if new_fleet_allocation:
                    new_fleet_allocation = json.loads(dumps(new_fleet_allocation))

                    if allocated_fleet:
                        allocated_fleet = json.loads(dumps(allocated_fleet))
                        allocated_fleet = allocated_fleet[0]

                        return jsonify({
                            "status": "200",
                            "message": "fleet_allocation_created_ok",
                            "data": allocated_fleet
                        })

                    else:
                        return jsonify({
                            "status": "404",
                            "message": "allocated_fleet_not_found",
                            "data": []
                        })

                else:

                    return jsonify({
                        "status": "404",
                        "message": "fleet_allocation_created_not_found",
                        "data": []
                    })

            except:
                traceback.print_exc()

                return jsonify({
                    "status": "500",
                    "message": "new_fleet_allocation_failed",
                    "data": []
                })

        except:
            traceback.print_exc()

            return jsonify({
                "status": "500",
                "message": "allocate_fleet_failed",
                "data": []
            })

    except:
        traceback.print_exc()

        return jsonify({
            "status": "500",
            "message": "allocate_conductor_failed",
            "data": []
        })