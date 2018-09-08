#  importing db
from . import db
# security model providing haching functionality
from werkzeug.security import generate_password_hash,check_password_hash


class User(db.Model):
    """
    creating class user for creating new users and connecting it to database via db.Model

    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    age = db.Column(db.String(255))
    pitch = db.relationship('pitches', backref = 'user', lazy='dynamic')
    comment = db.relationship('comment', backref = 'user', lazy='dynamic')
    upvote = db.relationship('Upvote', backref='user', lazy='dynamic')
    downvote = db.relationship('downvote', backref='user', lazy='dynamic')

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    """
    creating connection between roles and users using ForeignKey to reference primary key in roles.id
    """
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    """
    creating columns, with primary key set as true
    
    """

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
    comment_id = db.relationship('Comment', backref='pitches', lazy='dynamic')
    upvote = db.relationship('Upvote', backref='pitches', lazy='dynamic')
    downvote = db.relationship('downvote', backref='pitches', lazy='dynamic')

    """
    using db relationship to create a virtual column connecting with the foreign key
    backref used to get the pitches specific to a user
    
    """

    def __repr__(self):
        return f'User {self.promotion.pickup.business.motivational}'


class Roles(db.Model):
    """
    class roles to create user roles

    """
    __tablname__ = 'roles'
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
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

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


class Downvote(db.Model):
    """
    class downvote tp create downvote table
    """
    id = db.Column(db.Integer, primary_key = True)
    downvote = db.Column(db.Integer)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))