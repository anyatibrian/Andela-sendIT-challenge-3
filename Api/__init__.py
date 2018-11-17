from flask import Flask
from config import app_config


def create_app(config_name):
    """function that create a flask app instance"""
    app = Flask(__name__)
    # registering the blueprint objects
    from Api.api_v1 import api_v1
    app.register_blueprint(api_v1, url_prefix='/api/v1')
    # accessing our configurations from the config file
    app.config.from_object(app_config[config_name])
    return app
