from ..api_v1 import api_v1
from flask import jsonify, request
from Api.models.parcel_orders import ParcelOrders
from flask_jwt_extended import jwt_required, get_jwt_identity


@api_v1.route('/parcels', methods=['POST'])
@jwt_required
def post_parcels():
    current_user = get_jwt_identity()
    json_data = request.get_json(force=True)
    orders = ParcelOrders()

    # creates parcels orders
    orders.create_parcel_order(name=json_data['parcel_name'],
                               destination=json_data['destination'],
                               description=json_data['description'],
                               pickup=json_data['pickup'],
                               user_id=current_user['user_id'])
    return jsonify({'message':"parcel order created successfully"}), 201
