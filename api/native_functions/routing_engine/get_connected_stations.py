import json

from bson.json_util import dumps
from bson.objectid import ObjectId

from ...configurations.database import mongo

def get_connected_stations():
    connected_stations = mongo.db.connected_stations.find({
        "record_status": "ACTIVE",
    })

    if connected_stations:
        connected_stations = json.loads(dumps(connected_stations))
        # return jsonify({
        #     "status": "200",
        #     "message": "stations_retrieved_ok",
        #     "data": stations
        # })
        
        # print(connected_stations)
        return connected_stations

    else:
        # return jsonify({
        #     "status": "404",
        #     "message": "stations_not_found",
        #     "data": []
        # })

        print("No stations")