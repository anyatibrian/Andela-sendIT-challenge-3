from Api.api_v1 import api_v1
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity


@api_v1.route('/parcels/<int:parcelId>/destination', methods=['PUT'])
@jwt_required
def edit_parcel_destination(parcel_id):
    current_user = get_jwt_identity()
    return jsonify({'user_info': current_user})