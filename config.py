import os


class Config:
    """
    general configuration parent class

    """
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://eugene:necromancer@localhost/final'
    SECRET_KEY = os.environ.get('SECRET_KEY')

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CON = True


class ProdConfig(Config):
    """
    production configuration child class
    """
    SQLALCHEMY_DATABASE_URL = 'HEROKU_POSTGRESQL_BROWN_URL'

    SECRET_KEY = os.environ.get('SECRET_KEY')


class TestConfig(Config):
    """
    tests configuration class
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://eugene:necromancer@localhost/pitches_test'


class DevConfig(Config):
    """
    development configuration child class

    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://eugene:necromancer@localhost/final'
    DEBUG = True


config_options={
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}