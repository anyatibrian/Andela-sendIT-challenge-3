from Api.api_v1 import api_v1
from flask import jsonify
from Api.models.parcel_orders import ParcelOrders
from flask_jwt_extended import get_jwt_identity, jwt_required


@api_v1.route('/parcels', methods=['GET'])
@jwt_required
def get_parcel_orders():
    current_user = get_jwt_identity()
    # accessing the parcels class
    orders = ParcelOrders()
    parcels = orders.get_users_parcel_orders(current_user['user_id'])
    if parcels:
        return jsonify({'parcel_orders': parcels}), 200
    return jsonify({'parcel_orders': 'your order is empty'}), 404


@api_v1.route('/parcels/<int:parcel_id>', methods=['GET'])
@jwt_required
def get_single_parcel_order(parcel_id):
    current_user = get_jwt_identity()

    parcel_order = ParcelOrders().get_single_parcel_orders(current_user['user_id'], parcel_id)
    if parcel_order:
        return jsonify({'parcel_order': parcel_order})
    return jsonify({'error': 'parcel order not found'}), 404
