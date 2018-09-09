from flask_login import login_required

from flask import render_template, request, redirect, url_for, abort

from ..models import Reviews, User


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
