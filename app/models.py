#  importing db
from . import db


class User(db.model):
    """
    creating class user for creating new users and connecting it to database via db.Model

    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    age = db.Columns(db.String(255))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
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


class Pitches(db.model):
    """
    creating class pitches for creating new pitches and categories

    """
    __tablename__ = "pitches"
    id = db.Column(db.Integer, primary_Key=True)
    promotion = db.Column(db.String(255))
    pickup = db.Column(db.String(255))
    business = db.Column(db.String(255))
    motivational = db.Column(db.String(255))
    users = db.relationship('User', backref='pitch', lazy='dynamic')
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
    name = db.Column(db.Integer(255))
    users = db.relationship('User', backref='role', lazy='dynamic')
    """
    creating relationship between users and pitches connecting with foreign key 
    
    """

    def __repr__(self):
        return f'User {self.name}'

