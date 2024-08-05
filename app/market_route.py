from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token

market_blueprint = Blueprint('market', __name__)

@market_blueprint.route("/products", methods=[])
def product():
 pass