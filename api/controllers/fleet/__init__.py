from flask import Blueprint, jsonify

fleet_blueprint = Blueprint("fleet_blueprint", __name__)

from . import get_fleets
from . import create_fleet
from . import allocate_fleet
from . import deallocate_fleet