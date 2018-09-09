from flask_login import login_required, current_user

from flask import render_template, redirect, request, url_for, abort

from ..models import User, Pitches, Comments

from . import main

from .forms import UpdateProfile, PitchForm

# import photos instance
from .. import db, photos


@main.route('/')
def index():

    title = 'PITCHES'

    return render_template('index.html', title=title)


@main.route('/user/<uname>')
def profile(uname):
    """
    profile name function
    :param uname:
    :return:
    """
    user = User.query.filter_by(username = uname).first()
    """
    querying database to find user according to username passed
    """
    if user is None:
        """
        calling abort if no user is found
        """
        abort(404)

    # template rendering when user is found and passing in of user a a variable
    return render_template("profile/profile.html", user = user)


@main.route('user/<uname>/update', methods = ['GET', 'POST'])
@login_required
def update_profile(uname):
    """
    function to take in username and instantiates the UpdateProfile class
    :param uname:
    :return:
    """
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        """
        validate content of user.bio to fill in what user has submitted
        """
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        # redirecting user back to login page
        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form =form)


# route processing form submission request accepting only post requests
@main.route('/user/<uname>/update/pic',methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    """
    querying database to pick user with username passed in
    """
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        """
        request function to check in any parameter with name photo passed into request
        save method to save file into application
        """
        path = f'photos/{filename}'
        user.profile_pic_path = path
        """
        update profile pic path property in user table and store path to the file
        """
        db.session.commit()
        """
        committing changes to database and redirect user to profile page
        """
    return redirect(url_for('main.profile', uname=uname))


# display pitches and pitch categories
@main.route('/pitch', methods=['GET', 'POST'])
def pitch():
    """
    function to display pitch form
    """
    pitch = Pitches()
    if pitch.validate_on_submit():

        pitches = Pitches(pitches=pitch.pitches.data, category=pitch.category.data)
        pitches.save_pitch()
        return redirect(url_for('main.index'))

    return render_template('new-pitch.html',pitch=pitch)


@main.route('/Promotional', methods = ['GET', 'POST'])
def promote():
    """
    displaying promotional pitches
    """
    promotional=Pitches.query.filter_by(category="Promotional").all()

    return render_template('promotional.html', pitches =promotional)


@main.route('/product', methods = ['GET', 'POST'])
def product():
    """
    show product pitches
    """
    product = Pitches.query.filter_by(category="Product").all()

    return render_template('product.html', pitches=product)


@main.route('/Religious', methods = ['GET', 'POST'])
def religious():
    """
     show religious pitches
    """
    religious = Pitches.query.filter_by(category="Religious").all()

    return render_template('Religious.html', pitches=religious)


@main.route('/Motivational', methods = ['GET', 'POST'])
def motivational():
    """
    show motivational pitches
    """
    motivational = Pitches.query.filter_by(category='Motivational').all()

    return render_template('Motivational.html', pitches=motivational)


# display comments
@main.route('/comments', methods = ['GET', 'POST'])
@login_required
def comments():
    """
    show comments
    """
    comment = Comments()
    if comment.validate_on_submit():

        comments = Comments(saying=comment.saying.data)
        comments.save_comments()
        return redirect(url_for('main.new-pitch'))

    return render_template('comments.html', comment=comment)