from Api.api_v1 import api_v1
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from Api.models.parcel_orders import ParcelOrders


@api_v1.route('/parcels/<int:parcelId>', methods=['PUT'])
@jwt_required
def edit_parcel_destination(parcelId):
    current_user = get_jwt_identity()
    json_data = request.get_json(force=True)
    try:
        destination = json_data['destination']
        parcels = ParcelOrders().update_parcel_destination(user_id=current_user['user_id'],
                                                           destination=destination,
                                                           parcel_id=parcelId)
        return jsonify({'message': 'parcel destination updated successfully'}), 201
    except Exception as error:
        print(error)
    return jsonify({'error': 'check your columns'}), 400
