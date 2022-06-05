import json
import traceback
import time

from flask import jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId
from datetime import datetime

from ..configurations.database import mongo

def find_next_station_status(next_station_id, date_format, now):
    try:
        next_station = mongo.db.station.find_one({
            "$and": [
                {"_id": ObjectId(next_station_id)},
                {"record_status": "ACTIVE"}
            ]
        })

        print(next_station)

        if next_station:
            next_last_pickup_time = datetime.strptime(next_station["last_pickup_time"], date_format)
            next_last_pickup_time = time.mktime(next_last_pickup_time.timetuple())

            time_interval_minutes = (now - next_last_pickup_time) / 60

            print("Interval: {} minutes".format(time_interval_minutes))

            """
                -IF INTERVAL IS LESS THAN 2 MINUTES,
                -SEND AN ALERT THROUGH CHANNEL TO INFORM USER
            """

    except:
        traceback.print_exc()