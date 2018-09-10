#  importing db
from . import db
# security model providing haching functionality
from werkzeug.security import generate_password_hash, check_password_hash

# import class UserMixin
from flask_login import UserMixin

# import login manager
from . import login_manager

from datetime import datetime


class User(UserMixin, db.Model):
    """
    creating class user for creating new users and connecting it to database via db.Model

    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    age = db.Column(db.String(255))
    pitch = db.relationship('Pitches', backref = 'user', lazy='dynamic')
    comment = db.relationship('Comments', backref = 'user', lazy='dynamic')
    upvote = db.relationship('Upvote', backref='user', lazy='dynamic')
    downvote = db.relationship('Downvote', backref='user', lazy='dynamic')

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    """
    creating connection between roles and users using ForeignKey to reference primary key in roles.id
    """
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    # password_hash = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    """
    creating columns, with primary key set as true
    
    """

    # call back function retieving user id when unique identifier is passed
    @login_manager.user_loader # modifies load_user function passing in a user_id to query the database and get a user with IID
    def load_user(user_id):
        return User.query.get(int(user_id))


    # @property
    # def password(self):
    #     raise AttributeError('YOU CANNOT READ THE PASSWORD')
    def set_password(self,password):
        self.pass_secure = generate_password_hash(password)

    # @password.setter
    # def password(self, password):
    #     self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        """
        method to verify password
        :param password:
        :return:
        """
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        """
        repr method to make debugging easier
        :return:
        """
        return f'User {self.username}'


class Pitches(db.Model):
    """
    creating class pitches for creating new pitches and categories

    """
    __tablename__ = "pitches"
    id = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.String(255))
    pitch = db.Column(db.String(290))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comment_id = db.relationship('Comments', backref='pitches', lazy='dynamic')
    upvote = db.relationship('Upvote', backref='pitches', lazy='dynamic')
    downvote = db.relationship('Downvote', backref='pitches', lazy='dynamic')

    """
    using db relationship to create a virtual column connecting with the foreign key
    backref used to get the pitches specific to a user
    
    """
    def save_pitch(self):
        """
        method to save pitches
        """
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitch(cls, category):
        """
        method to return pitches

        """
        pitch = Pitches.query.filter_by(category=category).all()
        return pitch

    def __repr__(self):
        return f'User {self.category}'


class Roles(db.Model):
    """
    class roles to create user roles

    """
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref='role', lazy='dynamic')

    """
    creating relationship between users and pitches connecting with foreign key 
    
    """

    def __repr__(self):
        return f'User {self.name}'


class Comments(db.Model):
    """
    class Comments to create table for comments

    """
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key = True)
    saying = db.Column(db.String(267))
    time = db.Column(db.DateTime, default=datetime.utcnow)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_comments(self):
        """
        method to save comments
        """
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, id):
        """
        method to return comments
        """
        comments = Comments.query.filter_by(saying=id).all()
        return comments

    def __repr__(self):

        return f'User {self.saying}'


class Upvote(db.Model):
    """
    class to create upvote table

    """
    id = db.Column(db.Integer, primary_key =True)
    vote = db.Column(db.Integer)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_Upvote(self):
        """
        method to save upvotes
        """
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_Upvote(cls, id):
        """
        method to return upvote
        """
        upvote = Upvote.query.filter_by(vote=id).all()
        return upvote


class Downvote(db.Model):
    """
    class downvote tp create downvote table
    """
    id = db.Column(db.Integer, primary_key = True)
    downvote = db.Column(db.Integer)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_Downvote(self):
        """
        method to save upvotes
        """
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_Downvote(cls, id):
        """
        method to return upvote
        """
        upvote = Upvote.query.filter_by(downvote=id).all()
        return upvote
