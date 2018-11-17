def check_empty_fields(*args):
    """checks for an empty field"""
    for field in args:
        if field == '':
            return True


def validate_pwd_and_username(username, password):
    if len(username) > 5 and len(password) > 6:
        return True
