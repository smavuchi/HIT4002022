from flask import Blueprint, jsonify

possible_route_blueprint = Blueprint("possible_route_blueprint", __name__)

from . import create_possible_route
from . import get_optimal_route
from . import accept_route
from . import get_routes