from flask_wtf import FlaskForm

# inportation of input fields from
from wtforms import StringField, PasswordField,SubmitField,IntegerField

# importation of validators
from wtforms.validators import Required, Email, EqualTo

# import User model
from ..models import User


class RegisatrationForm(FlaskForm):
    """
    registration form class for creation of input fields

    """
    email= StringField('Input Email Address', validators=[Required(), Email()])
    username = StringField('Input username', validators = [Required()])
    age = IntegerField('age', validators=[Required()])
    password = PasswordField('Password', validators=[Required(), EqualTo('password_confirm', message='Passwords must match')])
    submit = SubmitField('SIGN UP')