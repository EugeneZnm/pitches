import flask_migrate import Migrate, MigrateCommand
from app import create_app,db
from app.models import User, Pitches, Comments, Upvote, Downvote, Roles
from flask_script import User, Role
from flask_script import Manager, Server

# Creating app instance
app = create_app('development')

# instantiate manager class
manager =Manager(app)

# command to launch application server
manager.add_command('server', Server)

#initialise migrate class in app instance
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

