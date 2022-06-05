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

def refresh_fleet(current_station, fleet_id, is_destination):
    try:
        if is_destination:
            mongo.db.fleet.update_one({
                    "_id": ObjectId(fleet_id),
                },

                {"$set": {
                    "current_station": ObjectId(current_station),
                    "fleet_status": "FREE",
                }
            })

        else:
            mongo.db.fleet.update_one({
                    "_id": ObjectId(fleet_id),
                },

                {"$set": {
                    "current_station": ObjectId(current_station),
                }
            })

        # refreshed_fleet = mongo.db.fleet.find_one({
        #     "$and": [
        #         {"_id": ObjectId(fleet_id)},
        #         {"record_status": "ACTIVE"}
        #     ]
        # })

        refreshed_fleet = mongo.db.fleet.aggregate(
            [
                {"$match": {"$and": [{"_id": ObjectId(fleet_id)}, {"record_status": "ACTIVE"}]}},

                # THERE IS NEED TO FILTER OUT 'PASSWORD', WILL BE BACK IN THE FUTURE...

                {"$lookup": {
                    "from": "station",
                    "foreignField": "_id",
                    "localField": "current_station",
                    "as": "current_station"
                }},

                {"$unwind": "$current_station"},
            ]
        )

        refreshed_fleet = json.loads(dumps(refreshed_fleet))
        refreshed_fleet = refreshed_fleet[0]

        pusher_client.trigger('passengers-prediction-channel', 'refresh-fleet', {"refreshed_fleet": refreshed_fleet})

        # print("REFRESHED STATION (funct): {}".format(refreshed_station))

        """
            -NOW SEND REFRESHED STATION TO CLIENT VIA OPEN CHANNEL **********************************************
            -WILL BE BACK SOON!!!!!
        """

        # return refreshed_station

    except:
        traceback.print_exc()
        # return {}