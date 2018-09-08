from flask import render_template, url_for, redirect
from . import auth

# imoort user model
from ..models import User
from ..forms import RegstrationForm
from .. import db


# view function
@auth.route('/login')
def login():
    """
    login function to render template file
    :return:
    """
    return render_template('auth/login.html')


@auth.route('register', methods=['GET', "POST"])
def register():
    """
    function to render registration form
    :return:
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, age=form.age.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        title = "Welcome New User"
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', registration_form = form)

