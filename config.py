import os
from os.path import dirname, join
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class BaseConfig:
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    DATABASE_URL = os.getenv('DEVELOPMENT_DATABASE')


class TestingConfig(BaseConfig):
    TESTING = True
    DATABASE_URL = os.getenv('TESTING_DATABASE')


class ProductionConfig(BaseConfig):
    DEBUG = False
    DATABASE_URL = os.getenv('DATABASE_URL')


app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}
