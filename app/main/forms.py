from flask_wtf import FlaskForm

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
    title = StringField('Something about your pitch', validators=[Required()])
    pitch = TextAreaField('Pitch Goes Here')
    category = RadioField('Categories', choices = [('Promotional', 'Promotional'),('Product', 'Product'),('Religious', 'Religious'), ('Motivational','Motivational')],validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    """
    class to create comment form
    """
    saying = TextAreaField('Write your comment')
    submit = SubmitField('Submit')


class UpVote(FlaskForm):
    submit = SubmitField('UPVOTE')


class DownVote(FlaskForm):
    submit = SubmitField('DOWNVOTE')