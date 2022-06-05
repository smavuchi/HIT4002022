from flask import jsonify
from . import live_feed_blueprint

@live_feed_blueprint.route("/predictions-feed")
def predictions_feed():
    return jsonify({
        "message": "predictions feed endpoint"
    })