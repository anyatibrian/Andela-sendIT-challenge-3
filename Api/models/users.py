from Api.models.database import DBConnect
from Api import create_app
import os

config_name = os.getenv("APP_SETTINGS")


class Users:
    def __init__(self, username, password, email):
        """function responsible for registering new users and login in existing users"""
        self.username = username
        self.password = password
        self.email = email
        self.app = create_app(config_name)
        self.conn = DBConnect(self.app.config['DATABASE_URL'])
        self.cursor = self.conn.cursor

