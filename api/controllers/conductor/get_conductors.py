import json

from flask import jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId

from . import conductor_blueprint
from ...configurations.database import mongo

@conductor_blueprint.route("/get-conductors")
def get_conductors():
    conductors = mongo.db.user.find(
        {"$and":
            [
                {"record_status": "ACTIVE"},
                {"role": "CONDUCTOR"}
            ],
        }
    )

    # conductors = mongo.db.conductor.aggregate(
    #     [
    #         {"$match": {"$and": [{"record_status": "ACTIVE"}]}},

    #         # THERE IS NEED TO FILTER OUT 'PASSWORD', WILL BE BACK IN THE FUTURE...
            
    #         {"$lookup": {
    #             "from": "user",
    #             "localField": "user_id",
    #             "foreignField": "_id",
    #             "as": "personal_details"
    #         }},

    #         {"$unwind": "$personal_details"}
    #     ]
    # )

    if conductors:
        conductors = json.loads(dumps(conductors))
        return jsonify({
            "status": "200",
            "message": "conductors_retrieved_ok",
            "data": conductors
        })

    else:
        return jsonify({
            "status": "404",
            "message": "conductors_not_found",
            "data": []
        })