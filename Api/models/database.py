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


