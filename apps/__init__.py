from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.debug = True
    config[config_name].init_app(app)
    db.init_app(app)


    from . blog import blogBlue
    app.register_blueprint(blogBlue)

    return app