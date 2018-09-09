from flask_login import login_required

from flask import render_template, redirect, url_for, abort

from ..models import User

from . import main

from .forms import UpdateProfile

from .. import db


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