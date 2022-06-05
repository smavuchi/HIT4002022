import json

from flask import jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId
from datetime import datetime

from . import waybill_blueprint
from ...configurations.database import mongo

@waybill_blueprint.route("/create-trip", methods=["POST"])
def create_trip():
    trip = request.json

    conductor_id = trip["conductor_id"]
    fleet_id = trip["fleet_id"]
    departure_time = datetime.now()
    departure_time = departure_time.strftime("%Y-%m-%d %H:%M:%S")
    # trip_origin =  trip["trip_origin"]
    # trip_destination =  trip["trip_destination"]
    head_count =  trip["head_count"]
    surplus_count =  trip["surplus_count"]
    route_allocation_id = trip["route_allocation_id"]
    live_route = trip["live_route"]
    trip_status = "LOADED"
    allocation_status = "ACCEPTED"

    for index, station in enumerate(live_route):
        live_route[index] = {
            # "station": station["station"],
            "station": station,
            "visited": "NO",
        }

    live_route_track = []

    for x in range(0, len(live_route)):
        live_route_track.append(x)


    trip_origin = live_route[0]["station"]
    trip_destination = live_route[-1]["station"]

    try:
        new_trip_id = mongo.db.trip.insert_one({
            "conductor_id": ObjectId(conductor_id),
            "fleet_id": ObjectId(fleet_id),
            "departure_time": departure_time,
            "arrival_time": "NOT_SET",
            "trip_origin": ObjectId(trip_origin),
            "trip_destination": ObjectId(trip_destination),
            "head_count": head_count,
            "surplus_count": surplus_count,
            "live_route": live_route,
            "live_route_track": live_route_track,
            "trip_status": trip_status,
            "creation_date": departure_time,
            "record_status": "ACTIVE"
        }).inserted_id

        """
            There is need to check if INSERT was successful or not before attempting to UPDATE Station.
            I WILL BE BACK!!!
            Possibly "DB Rollbacks"
        """

        # new_trip = mongo.db.trip.find_one({
        #     "$and": [
        #         {"_id": ObjectId(new_trip_id)},
        #         {"record_status": "ACTIVE"}
        #     ]
        # })

        new_trip = mongo.db.trip.aggregate(
            [
                {"$match": {"$and": [{"_id": ObjectId(new_trip_id)}, {"record_status": "ACTIVE"}]}},

                # THERE IS NEED TO FILTER OUT 'PASSWORD', WILL BE BACK IN THE FUTURE...

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

        if new_trip:
            """
                There is need to check if UPDATE was successful or not before proceeding.
                I WILL BE BACK!!!
                Possibly "DB Rollbacks"
            """
            mongo.db.station.update_one({
                "_id": ObjectId(live_route[0]["station"])
                },

                {"$set": {
                    "last_pickup_time": departure_time,
                    "last_pickup_fleet": fleet_id,
                }
            })

            mongo.db.fleet.update_one({
                "_id": ObjectId(fleet_id)
                },

                {"$set": {
                    # "active_trip_origin": trip_origin,
                    "fleet_status": "OCCUPIED"
                }
            })

            mongo.db.route_allocation.update_one({
                "_id": ObjectId(route_allocation_id)
                },

                {"$set": {
                    # "active_trip_origin": trip_origin,
                    "allocation_status": allocation_status
                }
            })

            new_trip = json.loads(dumps(new_trip))

            """
                There is need to TRIGGER a websocket alert to acknowledge DISPATCHER that Route Allocation was accepted.
            """

            return jsonify({
                "status": "200",
                "message": "trip_created_ok",
                "data": new_trip
            })

        else:

            return jsonify({
                "status": "404",
                "message": "trip_created_not_found",
                "data": []
            })

    finally:
        print("Database Error")