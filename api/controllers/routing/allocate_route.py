import os
import json
import pusher

from flask import jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId
from dotenv import load_dotenv
from datetime import datetime

from . import routing_blueprint
from ...configurations.database import mongo

# Environment Variables
load_dotenv()

pusher_client = pusher.Pusher(
  app_id=os.getenv("PUSHER_APP_ID"),
  key=os.getenv("PUSHER_KEY"),
  secret=os.getenv("PUSHER_SECRET"),
  cluster=os.getenv("PUSHER_CLUSTER"),
  ssl=True
)

@routing_blueprint.route("/allocate-route", methods=["POST"])
def allocate_route():
    route_allocation = request.json

    conductor_id = route_allocation["conductor_id"]
    fleet_id = route_allocation["fleet_id"]
    # route_request_id = route_allocation["route_request_id"]
    optimal_route = route_allocation["optimal_route"]
    allocation_status = "PENDING"

    # for index, station in enumerate(optimal_route):
    #     optimal_route[index] = ObjectId(station)

    creation_date = datetime.now()
    creation_date = creation_date.strftime("%Y-%m-%d %H:%M:%S")

    new_route_allocation_id = mongo.db.route_allocation.insert_one({
        "conductor_id": ObjectId(conductor_id),
        "fleet_id": ObjectId(fleet_id),
        "optimal_route": optimal_route,
        "allocation_status": allocation_status,
        "creation_date": creation_date,
        "record_status": "ACTIVE"
    }).inserted_id

    # new_route_allocation = mongo.db.route_allocation.find_one({
    #     "$and": [
    #         {"_id": ObjectId(new_route_allocation_id)},
    #         {"record_status": "ACTIVE"}
    #     ]
    # })

    new_route_allocation = mongo.db.route_allocation.aggregate(
        [
            {"$match": {"$and": [{"_id": ObjectId(new_route_allocation_id)}, {"record_status": "ACTIVE"}]}},

            # THERE IS NEED TO FILTER OUT 'PASSWORD', WILL BE BACK IN THE FUTURE...

            {"$lookup": {
                "from": "user",
                "foreignField": "_id",
                "localField": "conductor_id",
                "as": "conductor"
            }},
            {"$unwind": "$conductor"},

            {"$lookup": {
                "from": "fleet",
                "foreignField": "_id",
                "localField": "fleet_id",
                "as": "fleet"
            }},
            {"$unwind": "$fleet"},

            # {"$lookup": {
            #     "from": "station",
            #     "foreignField": "_id",
            #     "localField": "optimal_route",
            #     "as": "optimal_route_stations"
            # }},
            # {"$unwind": "$station"},
        ]
    )

    if new_route_allocation:

        # mongo.db.route_request.update_one({
        #     "_id": ObjectId(route_request_id)
        #     },

        #     {"$set": {
        #         "request_status": "ALLOCATED",
        #     }
        # })

        new_route_allocation = json.loads(dumps(new_route_allocation))
        print(new_route_allocation)
        new_route_allocation = new_route_allocation[0]

        # Send Route Allocation websocket alert to CONDUCTOR
        pusher_client.trigger('route-allocation-channel', 'route-allocation', {"new_route_allocation": new_route_allocation})

        return jsonify({
            "status": "200",
            "message": "route_allocation_created_ok",
            "data": new_route_allocation
        })

    else:

        return jsonify({
            "status": "404",
            "message": "route_allocation_created_not_found",
            "data": []
        })