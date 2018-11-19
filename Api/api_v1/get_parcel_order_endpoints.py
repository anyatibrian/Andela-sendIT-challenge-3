from Api.api_v1 import api_v1
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity,jwt_required


@api_v1.route('/parcels', methods=['GET'])
@jwt_required
def get_parcel_orders():
    current_user = get_jwt_identity()
