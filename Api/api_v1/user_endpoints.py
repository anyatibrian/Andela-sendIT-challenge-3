from ..api_v1 import api_v1
from flask import jsonify, request
from ..models.users import Users


@api_v1.route('auth/signup', methods=['POST'])
def register_user():
    json_data = request.get_json(force=True)
    users = Users()
    users.register_users(username=json_data['username'], password=json_data['password'], email=json_data['email'])
    return jsonify({'message': 'your account has been created successfully'})
