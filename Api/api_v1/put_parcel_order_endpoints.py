from Api.api_v1 import api_v1
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from Api.models.parcel_orders import ParcelOrders


@api_v1.route('/parcels/<int:parcel_id>/destination', methods=['PUT'])
@jwt_required
def update_parcel_destination(parcel_id):
    current_user = get_jwt_identity()
    json_data = request.get_json(force=True)

    destination = json_data['destination']
    if isinstance(destination, str):
        parcels = ParcelOrders().update_parcel_destination(user_id=current_user['user_id'],
                                                           destination=destination,
                                                           parcel_id=parcel_id)
        return jsonify({'message': 'parcel destination updated successfully'}), 201
    return jsonify({'error': 'destination should be strings only'}), 400


@api_v1.route('/parcels/<int:parcelId>/status', methods=['PUT'])
@jwt_required
def update_parcel_status(parcelId):
    pass