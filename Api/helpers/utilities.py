import re


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
