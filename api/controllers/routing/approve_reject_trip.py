from flask import jsonify
from . import routing_blueprint

@routing_blueprint.route("/approve-reject-trip")
def approve_reject_trip():
    return jsonify({
        "message": "approve/reject trip endpoint"
    })