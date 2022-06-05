from flask import Blueprint, jsonify

live_feed_blueprint = Blueprint("live_feed_blueprint", __name__)

from . import predictions_feed
from . import trips_feed