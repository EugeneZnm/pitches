from flask import render_template
from . import auth


@auth.route('/login')
def login():
    """
    login function to render template file
    :return:
    """
    return render_template('auth/login.html')