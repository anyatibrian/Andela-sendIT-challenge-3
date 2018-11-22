from flask import Blueprint

api_v1 = Blueprint('views', __name__)
from . import parcel_orders, users
