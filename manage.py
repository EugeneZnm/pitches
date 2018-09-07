from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)

    bootstrap.init_app(app)
    db.init_app(app)