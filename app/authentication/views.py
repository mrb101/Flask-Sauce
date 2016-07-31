from flask import render_template, redirect, url_for, flash, request
from sqlalchemy.orm.exc import NoResultFound
from . import authentication

from .forms import LoginForm
from .models import User
from flask.ext.login import (
    login_user,
    current_user,
    login_required,
    logout_user
    )


@authentication.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if request.method == 'POST':
        password = form.password.data
        username = form.username.data
        user = User.query.filter_by(username=username).first()
        if user is not None and user.verify_password(password) == True:
            flash('Welcome to Sauce')
            return redirect(url_for('authentication.register'))
        flash('Invalid Username or Password!')
        return redirect(url_for('authentication.login'))
    return render_template('authentication/login.html', form=form)


@authentication.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('authentication/register.html')


@authentication.route('/logout', methods=['GET'])
def logout():
    logout_user()
    flash('You have logged out!')
    return redirect(url_for('authentication.login'))
