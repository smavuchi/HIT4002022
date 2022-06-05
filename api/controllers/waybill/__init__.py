from flask import Blueprint, jsonify

waybill_blueprint = Blueprint("waybill_blueprint", __name__)

from . import create_trip
from . import get_trips
from . import get_my_trip
from . import update_trip
from . import delete_trip
from . import offload_trip