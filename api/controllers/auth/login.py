import json
import traceback

from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity
)
from bson.json_util import dumps
from bson.objectid import ObjectId

from . import auth_blueprint
from ...configurations.database import mongo

@auth_blueprint.route("/login", methods=["POST"])
def login():
    try:
        user = request.json
        email = user["email"]
        password = user["password"]
        print(user)

        user = mongo.db.user.find_one({
            "$and": [
                {"email": email},
                {"record_status": "ACTIVE"}
            ]
        })

        if user:
            user = json.loads(dumps(user))

            if user["password"] == password:
                user.pop("password")

                access_token = create_access_token(identity=user)

                return jsonify({
                    "status": "200",
                    "message": "{} {} you are now logged in".format(user["first_name"], user["last_name"]),
                    "token": access_token,
                })

            else:
                return jsonify({
                    "status": "401",
                    "message": "Incorrect credentials."
                })

        else:
            return jsonify({
                "status": "401",
                "message": "Incorrect credentials."
            })

    except:
        traceback.print_exc()

        return jsonify({
            "status": "500",
            "message": "Error encountered while connecting to user collection"
        })