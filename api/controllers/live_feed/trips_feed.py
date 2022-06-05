from flask import jsonify
from . import live_feed_blueprint

@live_feed_blueprint.route("/trips-feed")
def trips_feed():
    return jsonify({
        "message": "trips feed endpoint"
    })