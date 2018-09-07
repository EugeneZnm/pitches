#  importing db
from . import db


class User(db.model):
    """
    creating class user for creating new users and connecting it to database via db.Model

    """
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255), unique = True, index = True)
    age = db.Columns(db.String(255))
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