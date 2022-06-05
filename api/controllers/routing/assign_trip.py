from flask import jsonify
from . import routing_blueprint

@routing_blueprint.route("/assign-trip")
def assign_trip():
    return jsonify({
        "message": "assign trip endpoint"
    })