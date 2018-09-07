import flask_migrate import Migrate, MigrateCommand
from app import create_app,db
from app.models import User, Pitches, Comments, Upvote, Downvote, Roles
from flask_script import User, Role
from flask_script import Manager, Server

