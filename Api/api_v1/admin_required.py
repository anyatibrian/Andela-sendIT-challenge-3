from flask import jsonify
from functools import wraps
from flask_jwt_extended import get_jwt_identity, verify_fresh_jwt_in_request
from Api.models.users import Users


def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        verify_fresh_jwt_in_request()
        current_user = get_jwt_identity()
        user = Users().find_user(current_user['user_id'])
        admin = user['admin']
        if not admin:
            return jsonify({'message': 'You cant perform this action because you are unauthorised'}), 401
        return f(*args, **kwargs)

    return wrapper
