from Api.models.users import DBConnect
from datetime import datetime


class ParcelOrders:
    """class that handles the products"""

    def __init__(self):
        self.conn = DBConnect()

    def create_parcel_order(self, name, destination, description, pickup, user_id):
        """function that create products"""
        created_at = datetime.utcnow()
        status = 'pending'
        current_location = pickup
        delivery_price = "000"
        sql = "INSERT INTO parcel_orders(name, destination, description," \
              " pickup, status, current_location, delivery_price, created_at" \
              ", user_id) VALUES('{}','{}', '{}','{}','{}','{}','{}','{}','{}'" \
              ")".format(name, destination, description, pickup, status,
                         current_location, delivery_price, created_at, user_id)
        self.conn.cursor.execute(sql)
        return 'order created successfully created'

    def parcel_exist(self, parcel_name):
        """function that checks the parcel order exists"""
        sql = "SELECT * FROM parcel_orders WHERE name='{}'".format(parcel_name)
        self.conn.cursor.execute(sql)
        parcels = self.conn.cursor.fetchone()
        return parcels

    def get_users_parcel_orders(self, user_id):
        """function that fetches all parcel orders by a specific user"""
        sql = "SELECT * FROM parcel_orders WHERE user_id='{}'".format(user_id)
        self.conn.cursor.execute(sql)
        parcels = self.conn.cursor.fetchall()
        return parcels

    def get_single_parcel_orders(self, user_id, parcel_id):
        """ function that fetches a single products"""
        sql = "SELECT * FROM parcel_orders WHERE user_id ={}".format(user_id) + "and parcel_id ='{}'".format(parcel_id)
        self.conn.cursor.execute(sql)
        parcel_order = self.conn.cursor.fetchone()
        return parcel_order

    def update_parcel_destination(self, user_id, destination, parcel_id):
        """function that updates parcel destination"""
        sql = "UPDATE parcel_orders SET destination='{}'".format(destination) + " WHERE parcel_id='{}'" \
            .format(parcel_id) + " and user_id='{}'".format(user_id)
        self.conn.cursor.execute(sql)

    def update_parcel_delivery_status(self, user_id, status, parcel_id):
        """function that update parcel delivery status"""
        sql = "UPDATE parcel_orders SET status='{}'".format(status) + " WHERE parcel_id='{}'" \
            .format(parcel_id) + " and user_id='{}'".format(user_id)
        self.conn.cursor.execute(sql)

    def admin_update_parcel_delivery_status(self, status, parcel_id):
        """function that enables the admin to update delivery status"""
        sql = "UPDATE parcel_orders SET status='{}'".format(status) + " WHERE parcel_id='{}'".format(parcel_id)
        self.conn.cursor.execute(sql)

    def admin_update_parcel_delivery_present_location(self, present_location, parcel_id):
        """function that enables the admin to update delivery status"""
        sql = "UPDATE parcel_orders SET current_location='{}'".format(present_location) + " WHERE parcel_id='{}'"\
            .format(parcel_id)
        self.conn.cursor.execute(sql)