from Api.models.users import DBConnect
from datetime import datetime


class ParcelOrders:
    """class that handles the products"""

    def __init__(self):
        self.conn = DBConnect()

    def create_parcel_order(self, name, destination, descripition, pickup, user_id):
        """function that create products"""
        created_at = datetime.utcnow()
        status = 'pending'
        current_location = 'None'
        delivery_price = "000"
        sql = "INSERT INTO parcel_orders(name, destination, description," \
              " pickup, status, current_location, delivery_price, created_at" \
              ", user_id) VALUES('{}','{}', '{}','{}','{}','{}','{}','{}','{}'" \
              ")".format(name, destination, descripition, pickup, status,
                         current_location, delivery_price, created_at, user_id)
