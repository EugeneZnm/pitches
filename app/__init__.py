from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app(config_name):
    """
    application factory function
    :param config_name:
    :return:
    """
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    bootstrap.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/authenticate')
    """
    registering blueprint instance
    url_prefix adds prefix to all routes registered with blueprint
    
    """
    db.init_app(app)

    return app