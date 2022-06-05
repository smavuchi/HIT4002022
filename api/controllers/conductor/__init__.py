from flask import Blueprint, jsonify

conductor_blueprint = Blueprint("conductor_blueprint", __name__)

from . import get_conductors