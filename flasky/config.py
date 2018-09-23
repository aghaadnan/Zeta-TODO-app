from flask_sqlalchemy import SQLAlchemy

# app.config['SECRET_KEY'] = 'jababababajaja123'

class Config():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    @staticmethod
    def init_app(app):
        pass
class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgres://choletgo:rCfEt4VFo2CINIbMpAmwwhVFTwsT4rYx@pellefant.db.elephantsql.com:5432/choletgo'
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://choletgo:rCfEt4VFo2CINIbMpAmwwhVFTwsT4rYx@pellefant.db.elephantsql.com:5432/choletgo'
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://choletgo:rCfEt4VFo2CINIbMpAmwwhVFTwsT4rYx@pellefant.db.elephantsql.com:5432/choletgo'
config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig
}    