from Api.models.database import DBConnect
from datetime import datetime


class Users:
    def __init__(self):
        """class responsible for registering new users and login in existing users"""
        self.conn = DBConnect()

    def register_users(self, username, email, password):
        """function that registers users """
        created_at = datetime.utcnow()
        query = "INSERT INTO users(username, email, password, create_at)" \
                " VALUES('{}','{}','{}','{}')".format(username, email, password, created_at)
        self.conn.cursor.execute(query)

    def check_username_exist(self, email):
        """function that checks user exists"""
        sql = "SELECT * FROM users WHERE email='{}'".format(email)
        self.conn.cursor.execute(sql)
        row = self.conn.cursor.fetchone()
        return row

    def login_user(self, username, password):
        """login user"""
        sql = "SELECT * FROM users WHERE username='{}'".format(username) + "and password='{}'".format(password)
        self.conn.cursor.execute(sql)
        users = self.conn.cursor.fetchone()
        return users

    def find_user(self, user_id):
        """checks whether the user is admin or not"""
        sql = "SELECT * FROM users WHERE user_id='{}'".format(user_id)
        self.conn.cursor.execute(sql)
        role = self.conn.cursor.fetchone()
        return role
