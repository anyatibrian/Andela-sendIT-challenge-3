from Api import create_app
import os
from Api.models.database import DBConnect


config_name = os.getenv("APP_SETTINGS")
app = create_app(config_name)
print(config_name)

if __name__ == '__main__':
    db = DBConnect()
    db.create_tables()
    app.run()