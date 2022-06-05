import json
import traceback
import time

from flask import jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId
from datetime import datetime

from ..configurations.database import mongo

def refresh_trip_function(trip_id, live_route_track, live_route):
    try:
        mongo.db.trip.update_one({
                "_id": ObjectId(trip_id),
            },

            {"$set": {
                "live_route_track": live_route_track,
                "live_route": live_route,
            }
        })

        refreshed_trip = mongo.db.trip.aggregate(
            [
                {"$match": {"$and": [{"_id": ObjectId(trip_id)}]}},

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

        if refreshed_trip:
            refreshed_trip = json.loads(dumps(refreshed_trip))
            print("REFRESHED TRIP (funct): {}".format(refreshed_trip))
            return refreshed_trip

        else:
            refreshed_trip = []

    except:
        traceback.print_exc()