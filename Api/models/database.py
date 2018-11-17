from urllib.parse import urlparse
from psycopg2 import extras as RDC
import psycopg2


class DBConnect:
    def __init__(self, database_url):
        url_parse = urlparse(database_url)
        dbname = url_parse.path[1:]
        username = url_parse.username
        hostname = url_parse.hostname
        password = url_parse.password
        port = url_parse.port
        try:
            print('establishing '+database_url)
            self.connection = psycopg2.connect(
                database=dbname,
                user=username,
                host=hostname,
                password=password,
                port=port
            )
            print('successfully connected')
            self.connection.autocommit = True
            self.cursor = self.connection.cursor(cursor_factory=RDC.RealDictCursor)
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def create_tables(self):
        """function that tables in the database"""
        query = (
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
        self.cursor.execute(query)