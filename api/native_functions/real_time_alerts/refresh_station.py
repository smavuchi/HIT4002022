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

def refresh_station(station_id, last_pickup_time, last_pickup_fleet):
    try:
        mongo.db.station.update_one({
                "_id": ObjectId(station_id),
            },

            {"$set": {
                "last_pickup_time": last_pickup_time,
                "last_pickup_fleet": last_pickup_fleet,
            }
        })

        refreshed_station = mongo.db.station.find_one({
            "$and": [
                {"_id": ObjectId(station_id)},
                {"record_status": "ACTIVE"}
            ]
        })

        refreshed_station = json.loads(dumps(refreshed_station))

        pusher_client.trigger('passengers-prediction-channel', 'refresh-station', {"refreshed_station": refreshed_station})

        # print("REFRESHED STATION (funct): {}".format(refreshed_station))

        """
            -NOW SEND REFRESHED STATION TO CLIENT VIA OPEN CHANNEL **********************************************
            -WILL BE BACK SOON!!!!!
        """

        # return refreshed_station

    except:
        traceback.print_exc()
        # return {}