import json

from flask import jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId

from . import fleet_blueprint
from ...configurations.database import mongo

@fleet_blueprint.route("/get-fleets")
def get_fleets():
    fleets = mongo.db.fleet.aggregate(
        [
            {"$match": {"$and": [{"record_status": "ACTIVE"}]}},

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

    if fleets:
        fleets = json.loads(dumps(fleets))
        return jsonify({
            "status": "200",
            "message": "fleets_retrieved_ok",
            "data": fleets
        })

    else:
        return jsonify({
            "status": "404",
            "message": "fleets_not_found",
            "data": []
        })