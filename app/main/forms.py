from flask_wtf import FlaskForm

from flask import render_template, url_for, redirect, abort

from wtforms import StringField, TextAreaField, SubmitField


class UpdateProfile(FlaskForm):
    """
    class update profile to create form
    """
    bio = TextAreaField('Tell Us Something Interesting About You')
    submit = SubmitField('Submit')


