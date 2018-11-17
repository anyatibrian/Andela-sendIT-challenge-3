from ..api_v1 import api_v1
from flask import jsonify, request
from ..models.users import Users


@api_v1.route('auth/signup', methods=['POST'])
def register_user():
    json_data = request.get_json(force=True)
    users = Users()
    # checks where the user has been created already
    if users.check_username_exist(username=json_data['username'], email=json_data['email']):
        return jsonify({'message': 'username and password already taken'})
    users.register_users(username=json_data['username'], password=json_data['password'], email=json_data['email'])
    return jsonify({'message': 'your account has been created successfully'})
