import os
import json
import traceback
import time
import pusher

from flask import jsonify, request
from bson import json_util
from bson.json_util import dumps
from bson.objectid import ObjectId
from dotenv import load_dotenv
from datetime import datetime

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

def offload_trip_native(trip_id, fleet_id, arrival_time, trip_status):
    try:
        mongo.db.trip.update_one({
                "_id": ObjectId(trip_id),
            },

            {"$set": {
                "trip_status": trip_status,
                "arrival_time": arrival_time,
            }
        })

        offloaded_trip = mongo.db.trip.find_one({
            "$and": [
                {"_id": ObjectId(trip_id)},
                {"record_status": "ACTIVE"}
            ]
        })

        offloaded_trip = json.loads(dumps(offloaded_trip))

        if offloaded_trip:
            offloaded_trip = json.loads(dumps(offloaded_trip))

            mongo.db.fleet.update_one({
                "_id": ObjectId(fleet_id)
                },

                {"$set": {
                    "fleet_status": "FREE"
                }
            })

            return offloaded_trip

        # pusher_client.trigger('passengers-prediction-channel', 'refresh-station', {"refreshed_station": refreshed_station})

        # print("REFRESHED STATION (funct): {}".format(refreshed_station))

        """
            -NOW SEND REFRESHED STATION TO CLIENT VIA OPEN CHANNEL **********************************************
            -WILL BE BACK SOON!!!!!
        """

        # return refreshed_station

    except:
        traceback.print_exc()
        # return {}