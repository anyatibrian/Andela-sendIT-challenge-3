from ..api_v1 import api_v1
from datetime import timedelta
from flask import jsonify, request
from flask_jwt_extended import create_access_token
from ..models.users import Users
from Api.helpers.utilities import check_empty_fields, validate_pwd_and_username, \
    check_validity_of_mail


@api_v1.route('auth/signup', methods=['POST'])
def register_user():
    """endpoint for registering users"""
    json_data = request.get_json(force=True)
    users = Users()

    # checks for empty field
    if check_empty_fields(json_data['username'], json_data['email'], json_data['password']):
        return jsonify({'message': 'some fields are empty'}), 400

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
    return jsonify({'message': 'your account has been created successfully'}), 201


@api_v1.route('auth/login', methods=['POST'])
def login_user():
    """endpoint for loggin in users users"""
    json_data = request.get_json(force=True)
    login = Users()

    # validation for empty fields
    if check_empty_fields(json_data['username'], json_data['password']):
        return jsonify({'message': 'please enter your username and password'}), 400

    # checks logs the user in
    login_user = login.login_user(json_data['username'], json_data['password'])
    if login_user:
        # setting the token object
        token = {
            "user_id": login_user['user_id'],
            "email": login_user['email'],
            "admin": login_user['admin']
        }
        access_token = create_access_token(identity=token, expires_delta=timedelta(hours=3))
        return jsonify({'access-token': access_token}), 200
    return jsonify({'message': 'username and password does not exist'}), 401
