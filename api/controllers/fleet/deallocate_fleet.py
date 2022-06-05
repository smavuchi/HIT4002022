import json
import traceback

from flask import jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId
from datetime import datetime

from . import fleet_blueprint
from ...configurations.database import mongo

@fleet_blueprint.route("/deallocate-fleet", methods=["PUT"])
def deallocate_fleet():
    fleet = request.json

    fleet_allocation_id = fleet["fleet_allocation_id"]
    conductor_id = fleet["conductor_id"]
    fleet_id = fleet["fleet_id"]
    allocation_date = datetime.now()
    allocation_date = allocation_date.strftime("%Y-%m-%d %H:%M:%S")

    try:
        mongo.db.conductor.update_one({
                "_id": ObjectId(conductor_id),
            },

            {"$set": {
                "allocation_status": "FREE",
            }
        })

        try:
            mongo.db.fleet.update_one({
                    "_id": ObjectId(fleet_id),
                },

                {"$set": {
                    "allocation_status": "FREE",
                }
            })

            try:
                mongo.db.fleet_allocation.update_one({
                        "_id": ObjectId(fleet_allocation_id),
                    },

                    {"$set": {
                        "record_status": "DELETED",
                    }
                })

                deleted_fleet_allocation = mongo.db.fleet_allocation.find_one({"_id": ObjectId(fleet_allocation_id)})

                if deleted_fleet_allocation:
                    deleted_fleet_allocation = json.loads(dumps(deleted_fleet_allocation))

                    return jsonify({
                        "status": "200",
                        "message": "fleet_allocation_deleted_ok",
                        "data": deleted_fleet_allocation
                    })

                else:

                    return jsonify({
                        "status": "404",
                        "message": "fleet_allocation_not_found",
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