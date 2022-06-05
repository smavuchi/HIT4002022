import json

from flask import jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId

from . import waybill_blueprint
from ...configurations.database import mongo

@waybill_blueprint.route("/get-my-trip/<conductor_id>")
def get_my_trip(conductor_id):
    # trips = mongo.db.trip.find({
    #     "record_status": "ACTIVE",
    # })

    my_trip = mongo.db.trip.aggregate(
        [
            {"$match": {"$and": [{"record_status": "ACTIVE"}, {"conductor_id": ObjectId(conductor_id)}, {"trip_status": "LOADED"}]}},

            # THERE IS NEED TO FILTER OUT 'PASSWORD', WILL BE BACK IN THE FUTURE...
            # IT SHOULD RETURN ONLY ONE MATCHING RECORD, NOT ALL...

            {"$lookup": {
                "from": "user",
                "localField": "conductor_id",
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

    if my_trip:
        my_trip = json.loads(dumps(my_trip))
        return jsonify({
            "status": "200",
            "message": "my_trip_retrieved_ok",
            "data": my_trip
        })

    else:
        return jsonify({
            "status": "404",
            "message": "my_trip_not_found",
            "data": []
        })