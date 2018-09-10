from flask_wtf import FlaskForm

from flask import render_template, url_for, redirect, abort

from wtforms import StringField, TextAreaField, SubmitField, RadioField, TextField

from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    """
    class update profile to create form
    """
    bio = TextAreaField('Tell Us Something Interesting About You')
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):
    """
    class to create pitch form
    """
    title = TextField('Something about your pitch', validators=[Required()])
    pitch = TextAreaField('Pitch Goes Here')
    category = RadioField('Categories', choices = [('Promotional', 'Promotional'),('Product', 'Product'),('Ideas', 'Ideas'), ('Motivational','Motivational')],validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    """
    class to create comment form
    """
    title = StringField('comment here', validators=[Required()])
    comment = TextAreaField('Write your comment')
    submit = SubmitField('Submit')
