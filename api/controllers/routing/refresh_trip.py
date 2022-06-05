import json
import traceback
import time

from flask import jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId
from datetime import datetime

from . import routing_blueprint
from ...configurations.database import mongo

# Native Functions
from ...native_functions.real_time_alerts.refresh_station import refresh_station
from ...native_functions.real_time_alerts.refresh_fleet import refresh_fleet
from ...native_functions.refresh_trip_function import refresh_trip_function
from ...native_functions.find_next_station_status import find_next_station_status
from ...native_functions.real_time_alerts.offload_trip import offload_trip_native

@routing_blueprint.route("/refresh-trip", methods=["PUT"])
def refresh_trip():
    trip = request.json
    date_format = "%Y-%m-%d %H:%M:%S"

    trip_id = trip["trip_id"]
    live_route_track = trip["live_route_track"]
    live_route = trip["live_route"]
    station_id = live_route[live_route_track[0]]["station"]
    last_pickup_fleet = trip["last_pickup_fleet"]
    last_pickup_time = datetime.now()
    last_pickup_time = last_pickup_time.strftime(date_format)
    
    now = datetime.now()
    now = time.mktime(now.timetuple())

    if len(live_route_track) > 1:
        next_station_id = live_route[1]["station"]

        try:
            refresh_station(station_id=station_id, last_pickup_time=last_pickup_time, last_pickup_fleet=last_pickup_fleet)
            refresh_fleet(current_station=station_id, fleet_id=last_pickup_fleet, is_destination=False)

            try:
                live_route[live_route_track[0]]["visited"] = "YES"
                live_route_track.pop(0)

                refreshed_trip = refresh_trip_function(trip_id=trip_id, live_route_track=live_route_track, live_route=live_route)

                # find_next_station_status(next_station_id=next_station_id, date_format=date_format, now=now)

                return jsonify({
                    "status": "200",
                    "message": "trip_refreshed_ok",
                    "data": refreshed_trip
                })

            except:
                traceback.print_exc()

                return jsonify({
                    "status": "500",
                    "message": "refresh_trip_status_failed",
                    "data": []
                })

        except:
            traceback.print_exc()

            return jsonify({
                "status": "500",
                "message": "refresh_station_status_failed",
                "data": []
            })

    elif len(live_route_track) == 1:
        try:
            refresh_station(station_id=station_id, last_pickup_time=last_pickup_time, last_pickup_fleet=last_pickup_fleet)
            refresh_fleet(current_station=station_id, fleet_id=last_pickup_fleet, is_destination=True)
            offload_trip_native(trip_id=trip_id, fleet_id=last_pickup_fleet, arrival_time=last_pickup_time, trip_status="OFFLOADED")

            try:
                live_route[live_route_track[0]]["visited"] = "YES"
                live_route_track.pop(0)

                refreshed_trip = refresh_trip_function(trip_id=trip_id, live_route_track=live_route_track, live_route=live_route)

                return jsonify({
                    "status": "200",
                    "message": "trip_refreshed_ok",
                    "data": refreshed_trip
                })

            except:
                traceback.print_exc()

                return jsonify({
                    "status": "500",
                    "message": "refresh_trip_status_failed",
                    "data": []
                })

        except:
            traceback.print_exc()

            return jsonify({
                "status": "500",
                "message": "refresh_station_status_failed",
                "data": []
            })

    else:
        return jsonify({
            "status": "500",
            "message": "route_has_no_stations",
            "data": []
        })