import json

from flask import jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId

from . import routing_blueprint
from ...configurations.database import mongo

@routing_blueprint.route("/get-route-allocations/<conductor_id>")
def get_route_allocations(conductor_id):
    # trips = mongo.db.trip.find({
    #     "record_status": "ACTIVE",
    # })

    route_allocations = mongo.db.route_allocation.aggregate(
        [
            {"$match": {"$and": [{"record_status": "ACTIVE"}, {"conductor_id": ObjectId(conductor_id)}, {"allocation_status": "PENDING"}]}},

            # THERE IS NEED TO FILTER OUT 'PASSWORD', WILL BE BACK IN THE FUTURE...

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
        ]
    )

    if route_allocations:
        route_allocations = json.loads(dumps(route_allocations))
        return jsonify({
            "status": "200",
            "message": "route_allocations_retrieved_ok",
            "data": route_allocations
        })

    else:
        return jsonify({
            "status": "404",
            "message": "route_allocations_not_found",
            "data": []
        })