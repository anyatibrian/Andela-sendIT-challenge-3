import re
from functools import wraps
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from Api.models.users import Users

def check_empty_fields(*args):
    """checks for an empty field"""
    for field in args:
        if field == '':
            return True


def validate_pwd_and_username(username, password):
    """check the length of username and password"""
    return len(username) > 5 and len(password) > 6


def check_validity_of_mail(email):
    """validates email"""
    return re.match(
        '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
        email)


def string_validator(string_param):
    special_characters = '$#@%&*!?'

    special_character = 0

    for character in string_param:
        if special_characters.find(character) != -1:
            special_character += 1

    if special_character >= 1:
        return True


def check_white_space_infield(*fields):
    for field in fields:
        if not field.strip():
            return True


def validate_order_delivery_status(status):
    if status != 'canceled' and status != 'pending':
        return True


def validate_order_delivery_status_by_admin(status):
    if status != 'Transit' and status != 'Delivered':
        return True
