from ..api_v1 import api_v1
from flask import jsonify, request
from ..models.users import Users
from Api.utilities import check_empty_fields


@api_v1.route('auth/signup', methods=['POST'])
def register_user():
    json_data = request.get_json(force=True)
    users = Users()

    # checks for empty field
    if check_empty_fields(json_data['username'], json_data['email'], json_data['password']):
        return jsonify({'message': 'please enter your username, email and password'})

    # checks where the user has been created already
    if users.check_username_exist(username=json_data['username'], email=json_data['email']):
        return jsonify({'message': 'username and password already taken'})

    users.register_users(username=json_data['username'], password=json_data['password'], email=json_data['email'])
    return jsonify({'message': 'your account has been created successfully'})
