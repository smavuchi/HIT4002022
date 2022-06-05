import json

from flask import jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId

from . import user_blueprint
from ...configurations.database import mongo

@user_blueprint.route("/get-users")
def get_users():
    users = mongo.db.user.find(
        {"$and":
            [
                {"record_status": "ACTIVE"},
            ],
        }
    )

    if users:
        users = json.loads(dumps(users))
        return jsonify({
            "status": "200",
            "message": "users_retrieved_ok",
            "data": users
        })

    else:
        return jsonify({
            "status": "404",
            "message": "users_not_found",
            "data": []
        })