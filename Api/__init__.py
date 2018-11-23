from flask import Flask
from flask_jwt_extended import JWTManager
from flasgger import Swagger


def create_app():
    """function that create a flask app instance"""
    app = Flask(__name__, instance_relative_config=True)
    # registering the blueprint objects
    Swagger(app)
    from Api.views import api_v1
    app.register_blueprint(api_v1, url_prefix='/api/v1')
    # configuring JWT
    app.config['JWT_SECRET_KEY'] = 'super-heros-save-the-world'
    jwt = JWTManager(app)
    return app
