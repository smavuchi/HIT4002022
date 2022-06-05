import json
import traceback
import time

from flask import jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId
from datetime import datetime

from . import waybill_blueprint
from ...configurations.database import mongo

from ...native_functions.real_time_alerts.offload_trip import offload_trip_native

@waybill_blueprint.route("/offload-trip", methods=["PUT"])
def offload_trip():
    trip = request.json
    date_format = "%Y-%m-%d %H:%M:%S"

    trip_id = trip["trip_id"]
    fleet_id = trip["fleet_id"]
    arrival_time = datetime.now()
    arrival_time = arrival_time.strftime(date_format)
    trip_status = "OFFLOADED"

    offloaded_trip = offload_trip_native(trip_id, fleet_id, arrival_time, trip_status)

    # try:
    #     mongo.db.trip.update_one({
    #             "_id": ObjectId(trip_id),
    #         },

    #         {"$set": {
    #             "trip_status": trip_status,
    #             "arrival_time": arrival_time,
    #         }
    #     })

    #     offloaded_trip = mongo.db.trip.find_one({
    #         "$and": [
    #             {"_id": ObjectId(trip_id)},
    #             {"record_status": "ACTIVE"}
    #         ]
    #     })

    if offloaded_trip:
        offloaded_trip = json.loads(dumps(offloaded_trip))

        mongo.db.fleet.update_one({
            "_id": ObjectId(fleet_id)
            },

            {"$set": {
                "fleet_status": "FREE"
            }
        })

        """
            There is need to TRIGGER a websocket alert to acknowledge DISPATCHER that trip was OFFLOADED.
        """

        return jsonify({
            "status": "200",
            "message": "trip_offloaed_ok",
            "data": offloaded_trip
        })

    else:
        return jsonify({
            "status": "404",
            "message": "trip_not_found",
            "data": []
        })

    # except:
    #     traceback.print_exc()