from Api.api_v1 import api_v1
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from Api.models.parcel_orders import ParcelOrders


@api_v1.route('/parcels/<int:parcelId>/destination', methods=['PUT'])
@jwt_required
def edit_parcel_destination(parcel_id):
    current_user = get_jwt_identity()
    json_data = request.get_json(force=True)
    parcels = ParcelOrders().update_parcel_destination(current_user['user_id'], parcel_id, json_data['destination'])
    return jsonify({'user_info': parcels})
