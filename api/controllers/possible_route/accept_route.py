import json

from flask import jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId

from . import possible_route_blueprint
from ...configurations.database import mongo

@possible_route_blueprint.route("/accept-route", methods=["POST"])
def accept_route():
    allocated_route = request.json

    route = allocated_route["route"]
    fleet = allocated_route["fleet"]

    new_allocated_route_id = mongo.db.routes_allocated.insert_one({
        "route": route,
        "fleet": fleet,
        "record_status": "ACTIVE"
    }).inserted_id

    new_allocated_route = mongo.db.routes_allocated.find_one({
        "$and": [
            {"_id": ObjectId(new_allocated_route_id)},
            {"record_status": "ACTIVE"}
        ]
    })

    if new_allocated_route:
        new_allocated_route = json.loads(dumps(new_allocated_route))

        return jsonify({
            "status": "200",
            "message": "route_allocated_ok",
            "data": new_allocated_route
        })

    else:

        return jsonify({
            "status": "404",
            "message": "route_allocated_not_found",
            "data": []
        })