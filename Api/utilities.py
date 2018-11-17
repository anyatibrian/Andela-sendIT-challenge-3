def check_empty_fields(*args):
    """checks for an empty field"""
    for field in args:
        if field == '':
            return True
