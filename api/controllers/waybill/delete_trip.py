import json

from flask import jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId

from . import waybill_blueprint
from ...configurations.database import mongo

@waybill_blueprint.route("/delete-trip/<trip_id>", methods=["DELETE"])
def delete_trip(trip_id):
    # trip = request.json
    
    # trip_id = trip["trip_id"]

    mongo.db.trip.update_one({
            "_id": ObjectId(trip_id),
        },

        {"$set": {
            "record_status": "DELETED",
        }
    })

    deleted_trip = mongo.db.trip.find_one({"_id": ObjectId(trip_id)})

    if deleted_trip:
        deleted_trip = json.loads(dumps(deleted_trip))

        return jsonify({
            "status": "200",
            "message": "trip_deleted_ok",
            "data": deleted_trip,
        })

    else:
        return jsonify({
            "status": "404",
            "message": "trip_not_found",
            "data": [],
        })