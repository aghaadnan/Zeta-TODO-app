from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
db = SQLAlchemy()
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])   
    # app.config.from_pyfile('config')
    config[config_name].init_app(app)
    with app.app_context():
        db.init_app(app)
    return app