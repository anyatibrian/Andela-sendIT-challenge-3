import os
from Api import create_app
from Api.models.database import DBConnect
from Api.models.users import Users


app = create_app()
user = Users()
print(os.getenv('APP_SETTINGS'))
if __name__ == '__main__':
    db = DBConnect()
    db.create_tables()
    user.create_default_admmin()
    app.run(debug=True)