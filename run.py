from Api import create_app
from Api.models.database import DBConnect
import os

app = create_app()
print(os.getenv('APP_SETTINGS'))
if __name__ == '__main__':
    db = DBConnect()
    db.create_tables()
    app.run(debug=True)