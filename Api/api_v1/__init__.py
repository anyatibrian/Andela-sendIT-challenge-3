from flask import Blueprint

api_v1 = Blueprint('api_v1', __name__)
from . import user_endpoints, admin_required, post_parcel_endpoints, \
    get_parcel_order_endpoints, put_parcel_order_endpoints
