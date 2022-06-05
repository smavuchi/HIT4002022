import json

from flask import jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId

from . import routing_blueprint
from ...configurations.database import mongo

@routing_blueprint.route("/get-route-requests")
def get_route_requests():
    # trips = mongo.db.trip.find({
    #     "record_status": "ACTIVE",
    # })

    route_requests = mongo.db.route_request.aggregate(
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
                "localField": "current_station",
                "foreignField": "_id",
                "as": "current_station"
            }},

            {"$unwind": "$current_station"},
        ]
    )

    if route_requests:
        route_requests = json.loads(dumps(route_requests))
        return jsonify({
            "status": "200",
            "message": "route_requests_retrieved_ok",
            "data": route_requests
        })

    else:
        return jsonify({
            "status": "404",
            "message": "route_requests_not_found",
            "data": []
        })