import json

from flask import jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId

from . import possible_route_blueprint
from ...configurations.database import mongo

@possible_route_blueprint.route("/get-routes")
def get_routes():
    # trips = mongo.db.trip.find({
    #     "record_status": "ACTIVE",
    # })

    # routes = mongo.db.possible_route.find({"record_status": "ACTIVE"})

    routes = mongo.db.route_allocation.aggregate(
        [
            {"$match": {"$and": [{"record_status": "ACTIVE"}]}},

            # THERE IS NEED TO FILTER OUT 'PASSWORD', WILL BE BACK IN THE FUTURE...

            {"$lookup": {
                "from": "station",
                "foreignField": "_id",
                "localField": "optimal_route",
                "as": "optimal_route_stations"
            }},
            # {"$unwind": "$station"},
        ]
    )

    if routes:
        routes = json.loads(dumps(routes))
        return jsonify({
            "status": "200",
            "message": "routes_retrieved_ok",
            "data": routes
        })

    else:
        return jsonify({
            "status": "404",
            "message": "routes_not_found",
            "data": []
        })