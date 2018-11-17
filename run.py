from Api import create_app
import os
config_name = os.getenv("APP_SETTINGS")
app = create_app(config_name)
print(config_name)

if __name__ == '__main__':
    app.run()