from Api import create_app
import pytest
from Api.models.database import DBConnect

empty_users = {
 "username": "anyatibrian",
 "email": "",
 "password": "password@123"
}


# creating our test client
@pytest.fixture(scope='module')
def client():
    app = create_app(config_name='testing')
    test_client = app.test_client()

    # creating the database object
    db = DBConnect()
    db.create_tables()
    # establishing the application context
    cxt = app.app_context()
    cxt.push()
    yield test_client
    db.drop_tables('users', 'parcel_orders')
    cxt.pop()
