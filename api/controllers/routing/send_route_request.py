import json
import traceback

from flask import jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId
from datetime import datetime

from . import routing_blueprint
from ...configurations.database import mongo

@routing_blueprint.route("/send-route-request", methods=["POST"])
def send_route_request():
    data = request.json

    user_id = data["user_id"]
    fleet_id = data["fleet_id"]
    current_station = data["current_station"]
    creation_date = datetime.now()
    creation_date = creation_date.strftime("%Y-%m-%d %H:%M:%S")
    request_status = "PENDING"

    try:
        new_route_request_id = mongo.db.route_request.insert_one({
            "user_id": ObjectId(user_id),
            "fleet_id": ObjectId(fleet_id),
            "current_station": ObjectId(current_station),
            "request_status": request_status,
            "creation_date": creation_date,
            "record_status": "ACTIVE"
        }).inserted_id

        new_route_request = mongo.db.route_request.aggregate(
            [
                {"$match": {"$and": [{"_id": ObjectId(new_route_request_id)}, {"record_status": "ACTIVE"}]}},

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

        if new_route_request:
            new_route_request = json.loads(dumps(new_route_request))

            return jsonify({
                "status": "200",
                "message": "route_request_sent_ok",
                "data": new_route_request
            })

        else:

            return jsonify({
                "status": "404",
                "message": "route_request_sent_not_found",
                "data": []
            })

    except:
        traceback.print_exc()

        return jsonify({
            "status": "404",
            "message": "route_request_sent_not_found",
            "data": []
        })