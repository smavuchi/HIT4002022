import json
import time

from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from bson.json_util import dumps
from bson.objectid import ObjectId

from ..configurations.database import mongo
from .predict_passengers import predict_passengers

def check_time_intervals():
    date_format = "%Y-%m-%d %H:%M:%S"
    now = datetime.now()
    now = time.mktime(now.timetuple())

    stations = mongo.db.station.find({
        "record_status": "ACTIVE",
    })

    # These Predictions should be absolutely persistent.
    predictions = []

    if stations:
        stations = json.loads(dumps(stations))

        for station in stations:
            if station["last_pickup_time"] != "NOT SET":
                trip_departure_time = datetime.strptime(station["last_pickup_time"], date_format)
                trip_departure_time = time.mktime(trip_departure_time.timetuple())

                time_interval_minutes = (now - trip_departure_time) / 60

                if time_interval_minutes >= 5:
                    prediction = predict_passengers(station)
                    predictions.append(prediction)
                # if trip["departure_time"]

            else:
                prediction = predict_passengers(station)
                predictions.append(prediction)

    print(predictions)
    # print(now)
    return predictions