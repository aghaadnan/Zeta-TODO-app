import os
from sqlalchemy import create_engine
# app.config['SECRET_KEY'] = 'jababababajaja123'

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    engine = create_engine('postgres://qumsyeohsjxyey:6731f62e36a6af93569215cebcfa6ce1c9f502c26f9150abde8de1a925cd643a@ec2-107-21-233-72.compute-1.amazonaws.com:5432/d25uh7eeg3qnhf')

    # SQLALCHEMY_DATABASE_URI = os.getenv("postgres://qumsyeohsjxyey:6731f62e36a6af93569215cebcfa6ce1c9f502c26f9150abde8de1a925cd643a@ec2-107-21-233-72.compute-1.amazonaws.com:5432/d25uh7eeg3qnhf")
    # conn =psycopg2.connect(DATABASE_URI,sslmode="require")
    @staticmethod
    def init_app(app):
        pass
class TestingConfig(Config):
    DEBUG = True
    TESTING = True


    
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass
config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig
}    