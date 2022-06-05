import json

from flask import jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId
from datetime import datetime

from . import possible_route_blueprint
from ...configurations.database import mongo

@possible_route_blueprint.route("/create-possible-route", methods=["POST"])
def create_possible_route():
    possible_route = request.json

    route = possible_route["route"]

    for index, station in enumerate(route):
        route[index] = ObjectId(station)

    creation_date = datetime.now()
    creation_date = creation_date.strftime("%Y-%m-%d %H:%M:%S")

    new_route_id = mongo.db.possible_route.insert_one({
        "route": route,
        "creation_date": creation_date,
        "record_status": "ACTIVE"
    }).inserted_id

    # new_route = mongo.db.possible_route.find_one({
    #     "$and": [
    #         {"_id": ObjectId(new_route_id)},
    #         {"record_status": "ACTIVE"}
    #     ]
    # })

    new_route = mongo.db.possible_route.aggregate(
        [
            {"$match": {"$and": [{"_id": ObjectId(new_route_id)}, {"record_status": "ACTIVE"}]}},

            # THERE IS NEED TO FILTER OUT 'PASSWORD', WILL BE BACK IN THE FUTURE...

            {"$lookup": {
                "from": "station",
                "foreignField": "_id",
                "localField": "route",
                "as": "route"
            }},
            # {"$unwind": "$station"},
        ]
    )

    if new_route:
        new_route = json.loads(dumps(new_route))

        return jsonify({
            "status": "200",
            "message": "possible_route_created_ok",
            "data": new_route
        })

    else:

        return jsonify({
            "status": "404",
            "message": "possible_route_created_not_found",
            "data": []
        })