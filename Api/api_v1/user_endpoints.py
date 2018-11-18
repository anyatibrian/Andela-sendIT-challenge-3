from ..api_v1 import api_v1
from flask import jsonify, request
from ..models.users import Users
from Api.utilities import check_empty_fields, validate_pwd_and_username, \
    check_validity_of_mail


@api_v1.route('auth/signup', methods=['POST'])
def register_user():
    json_data = request.get_json(force=True)
    users = Users()

    # checks for empty field
    if check_empty_fields(json_data['username'], json_data['email'], json_data['password']):
        return jsonify({'message': 'please enter your username, email and password'}), 400

    # checks the length of username and password
    if not validate_pwd_and_username(json_data['username'], json_data['password']):
        return jsonify({'message': 'username and password should be atleast six chars'}), 400

    # validates emails
    if not check_validity_of_mail(json_data['email']):
        return jsonify({'message': 'invalid email'}), 400
    # checks where the user has been created already
    user_exist = users.check_username_exist(email=json_data['email'])
    if user_exist:
        return jsonify({'message': user_exist['email'] + ' already taken'}), 400

    # handles user registrations
    users.register_users(username=json_data['username'],
                         password=json_data['password'],
                         email=json_data['email'])
    return jsonify({'message': 'your account has been created successfully'})
