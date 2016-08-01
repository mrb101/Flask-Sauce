from flask import render_template, redirect, url_for, flash, request
from app import db
from . import authentication

from .forms import LoginForm, RegisterForm
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
            login_user(user, form.remember_me.data)
            flash('Welcome to Sauce')
            return redirect(url_for('authentication.index'))
        flash('Invalid Username or Password!')
        return redirect(url_for('authentication.login'))
    return render_template('authentication/login.html', form=form)


@authentication.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        user = User()
        user.username = form.username.data
        user.name = form.name.data
        user.email = form.email.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash('You are registerd!')
        return redirect(url_for('main.index'))
    return render_template('authentication/register.html', form=form)


@authentication.route('/logout', methods=['GET'])
def logout():
    logout_user()
    flash('You have logged out!')
    return redirect(url_for('authentication.login'))
