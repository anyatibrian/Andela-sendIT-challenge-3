from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..api_v1 import api_v1
from Api.models.parcel_orders import ParcelOrders
from Api.helpers.utilities import check_empty_fields, string_validator,\
    check_white_space_infield, validate_order_delivery_status


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
        return jsonify({'error': 'white space chars not allowed'}), 400

    # check ing invalid chars
    if string_validator(json_data['description']):
        return jsonify({'errors': 'your description field has invalid chars'}), 400

    # checks order parcel exist
    if orders.parcel_exist(parcel_name=json_data['parcel_name']):
        return jsonify({'message': 'parcel order already exist'}), 400

    # creates parcels orders
    orders.create_parcel_order(name=json_data['parcel_name'].strip(),
                               destination=json_data['destination'].strip(),
                               description=json_data['description'].strip(),
                               pickup=json_data['pickup'].strip(),
                               user_id=current_user['user_id'])
    return jsonify({'message': "parcel order created successfully"}), 201


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
    current_user = get_jwt_identity()
    json_data = request.get_json(force=True)

    # validates status
    if validate_order_delivery_status(json_data['status']):
        return jsonify({'error': 'in valid status'}), 400
    ParcelOrders().update_parcel_delivery_status(current_user['user_id'], json_data['status'], parcelId)
    return jsonify({'message': 'status has been successfully updated'}), 201