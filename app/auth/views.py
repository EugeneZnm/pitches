from flask import render_template
from . import auth

# view function
@auth.route('/login')
def login():
    """
    login function to render template file
    :return:
    """
    return render_template('auth/login.html')