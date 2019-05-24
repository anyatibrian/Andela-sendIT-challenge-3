from psycopg2 import extras as RDC
import psycopg2
import os


class DBConnect:
    """class that establishes database connection, creates various tables and drops the tables """
    def __init__(self):
        if os.getenv('APP_SETTINGS') == "testing":
            DATABASE_URL = 'postgresql://postgres:password@127.0.0.1:5432/test_db'
        else:
            DATABASE_URL = 'postgres://iaohptvtbkmgka:081e5bae79f44c095654fc3b6ee29' \
                           '6fa0098b2ca6984d613012c59589254ca 62@ec2-50-19-249-121.' \
                           'compute-1.amazonaws.com:5432/d999nce7urgeak'
            #DATABASE_URL = 'postgresql://postgres:password@127.0.0.1:5432/sendIT'
        try:
            print('establishing connection made successfully')
            self.connection = psycopg2.connect(DATABASE_URL)
            print('successfully connected')
            self.connection.autocommit = True
            self.cursor = self.connection.cursor(cursor_factory=RDC.RealDictCursor)
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def create_tables(self):
        """function  that creates tables in the database"""
        queries = (
            """CREATE TABLE IF NOT EXISTS users(
            user_id serial PRIMARY KEY NOT NULL ,
            username VARCHAR(100)  NOT NULL,
            email VARCHAR(100)NOT NULL,
            password VARCHAR(100) NOT NULL,
            create_at VARCHAR(100) NOT NULL,
            admin BOOLEAN DEFAULT FALSE 
            )""",
            """
            CREATE TABLE IF NOT EXISTS parcel_orders(
            parcel_id serial PRIMARY KEY NOT NULL,
            receivers VARCHAR(100) NOT NULL,
            description VARCHAR(100) NOT NULL,
            destination VARCHAR(100) NOT NULL,
            pickup VARCHAR(200) NOT NULL,
            status VARCHAR(100) DEFAULT'pending',
            current_location VARCHAR(100) NOT NULL,
            delivery_price VARCHAR(100)NOT NULL,
            Serial_No VARCHAR(100) NOT NULL,
            weight INT NOT NULL,
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

    def drop_tables(self):
        """function that drops the tables"""
        query = "TRUNCATE TABLE users, parcel_orders RESTART IDENTITY "
        self.cursor.execute(query)
        return print('tables dropped successfully')
