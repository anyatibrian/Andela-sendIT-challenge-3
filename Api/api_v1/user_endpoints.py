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
    user_exist = users.check_username_exist(email=json_data['email'])
    if user_exist:
        return jsonify({'message': user_exist['email'] + ' already taken'})

    # handles user registrations
    users.register_users(username=json_data['username'].strip(),
                         password=json_data['password'].strip(),
                         email=json_data['email'].strip())
    return jsonify({'message': 'your account has been created successfully'})
