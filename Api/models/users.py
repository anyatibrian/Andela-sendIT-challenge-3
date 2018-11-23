from Api.models.database import DBConnect
from datetime import datetime


class Users:
    def __init__(self):
        """class responsible for registering new users and login in existing users"""
        self.conn = DBConnect()

    def register_users(self, username, email, password):
        """function that registers users """
        created_at = datetime.utcnow()
        sql = "INSERT INTO users(username, email, password, create_at)" \
              " VALUES('{}','{}','{}','{}')".format(username, email, password, created_at)
        self.conn.cursor.execute(sql)

    def check_username_exist(self, email):
        """function that checks validates"""
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

    def create_default_admmin(self):
        created_at = datetime.utcnow()
        sql = "SELECT * FROM users WHERE username='admin'"
        self.conn.cursor.execute(sql)
        result = self.conn.cursor
        if not result:
            sql = "INSERT INTO users(username, password, email,create_at, admin) VALUES('admin'," \
                  " 'admin@123', 'anyatibrian@gmail.com','{}',True)" \
                  "".format(created_at)
            self.conn.cursor.execute(sql)
            print('default admin created successfully')
        print('admin user already exist')
