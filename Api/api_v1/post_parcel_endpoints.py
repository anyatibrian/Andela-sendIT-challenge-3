from ..api_v1 import api_v1
from flask import jsonify, request
from Api.models.parcel_orders import ParcelOrders
from flask_jwt_extended import jwt_required, get_jwt_identity
from Api.utilities import check_empty_fields, string_validator, check_white_space_infield


@api_v1.route('/parcels', methods=['POST'])
@jwt_required
def post_parcels():
    current_user = get_jwt_identity()
    json_data = request.get_json(force=True)
    orders = ParcelOrders()
    # checks for empty parcel  fields
    if check_empty_fields(json_data['parcel_name'], json_data['destination'],
                          json_data['description'], json_data['pickup']):
        return jsonify({'errors': 'fields must not be empty'}), 400

    # checks for white space chars
    if check_white_space_infield(json_data['parcel_name'], json_data['destination'],
                                 json_data['description'], json_data['pickup']):
        return jsonify({'error': 'white space chars not allowed'})

    # checking invalid chars
    if string_validator(json_data['description']):
        return jsonify({'errors': 'your description field has invalid chars'}), 400

    # checks order parcel exist
    if orders.parcel_exist(parcel_name=json_data['parcel_name']):
        return jsonify({'message': 'parcel order already exist'}), 401

    # creates parcels orders
    orders.create_parcel_order(name=json_data['parcel_name'].strip(),
                               destination=json_data['destination'].strip(),
                               description=json_data['description'].strip(),
                               pickup=json_data['pickup'].strip(),
                               user_id=current_user['user_id'])
    return jsonify({'message': "parcel order created successfully"}), 201
