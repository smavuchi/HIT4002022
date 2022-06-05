import json

from flask import jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId

from . import waybill_blueprint
from ...configurations.database import mongo

@waybill_blueprint.route("/get-trips")
def get_trips():
    # trips = mongo.db.trip.find({
    #     "record_status": "ACTIVE",
    # })

    trips = mongo.db.trip.aggregate(
        [
            {"$match": {"$and": [{"record_status": "ACTIVE"}]}},

            # THERE IS NEED TO FILTER OUT 'PASSWORD', WILL BE BACK IN THE FUTURE...

            {"$lookup": {
                "from": "user",
                "localField": "user_id",
                "foreignField": "_id",
                "as": "conductor"
            }},

            {"$unwind": "$conductor"},

            {"$lookup": {
                "from": "fleet",
                "localField": "fleet_id",
                "foreignField": "_id",
                "as": "fleet"
            }},

            {"$unwind": "$fleet"},

            {"$lookup": {
                "from": "station",
                "localField": "trip_origin",
                "foreignField": "_id",
                "as": "trip_origin"
            }},

            {"$unwind": "$trip_origin"},

            {"$lookup": {
                "from": "station",
                "localField": "trip_destination",
                "foreignField": "_id",
                "as": "trip_destination"
            }},

            {"$unwind": "$trip_destination"},
        ]
    )

    if trips:
        trips = json.loads(dumps(trips))
        return jsonify({
            "status": "200",
            "message": "trips_retrieved_ok",
            "data": trips
        })

    else:
        return jsonify({
            "status": "404",
            "message": "trips_not_found",
            "data": []
        })