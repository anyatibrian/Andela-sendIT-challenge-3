from psycopg2 import extras as RDC
import psycopg2
import os

from Api import create_app

config_name = os.getenv("APP_SETTINGS")


class DBConnect:
    def __init__(self):
        self.app = create_app(config_name)
        self.db_url = self.app.config['DATABASE_URL']
        try:
            print('establishing connection to' + self.db_url)
            self.connection = psycopg2.connect(self.db_url)
            print('successfully connected')
            self.connection.autocommit = True
            self.cursor = self.connection.cursor(cursor_factory=RDC.RealDictCursor)
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def create_tables(self):
        """function that tables in the database"""
        queries = (
            """CREATE TABLE IF NOT EXISTS users(
            user_id serial PRIMARY KEY NOT NULL ,
            username VARCHAR(100) UNIQUE NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(100) NOT NULL,
            create_at VARCHAR(100) NOT NULL,
            admin BOOLEAN DEFAULT TRUE 
            )""",
            """
            CREATE TABLE IF NOT EXISTS parcel_orders(
            parcel_id serial PRIMARY KEY NOT NULL,
            name VARCHAR(100) NOT NULL,
            description VARCHAR(100) NOT NULL,
            destination VARCHAR(100) NOT NULL,
            pickup VARCHAR(200) NOT NULL,
            status VARCHAR(100) DEFAULT'pending',
            current_location VARCHAR(100) NOT NULL,
            delivery_price VARCHAR(100)NOT NULL,
            created_at VARCHAR(100) NOT NULL,
            user_id INT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE 
            )
            """
        )
        # creating the tables
        for tables in queries:
            self.cursor.execute(tables)
        print("tables created successfully")

    def drop_tables(self, *tables):
        """function that drops the tables"""
        for table in tables:
            query = "DROP TABLE IF EXISTS {} CASCADE".format(table)
            self.cursor.execute(query)
        return print('tables dropped successfully')

    def execute(self, query):
        """function that handles the database query execution"""
        try:
            self.cursor.execute(query)
            return 'success'
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)