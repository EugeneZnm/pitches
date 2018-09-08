from flask import render_template, url_for, redirect, request, flash
from . import auth

# imoort user model
from ..models import User
from ..forms import RegstrationForm, LoginForm
from .. import db


# view function
@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    login function to render template file
    :return:
    """
    login_form=LoginForm()
    if login_form.validate_on_submit():
        user User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            retrun redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

     title = "watchlist login"
    return render_template('auth/login.html', login_form, title=title)


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

