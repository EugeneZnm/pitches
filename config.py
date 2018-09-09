import os


class Config:
    """
    general configuration parent class

    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://eugene:necromancer@localhost/pit1'
    SECRET_KEY = os.environ.get('SECRET-KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CON = True


class ProdConfig(Config):
    """
    production configuration child class
    """
    pass


class DevConfig(Config):
    """
    development configuration child class
    """

    DEBUG = True


config_options={
    'development': DevConfig,
    'production': ProdConfig
}