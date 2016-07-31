from flask import render_template, redirect, url_for
from . import authentication

@authentication.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('authentication/login.html')


@authentication.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('authentication/register.html')


@authentication.route('/logout', methods=['GET'])
def logout():
    return redirect(url_for('authentication.login'))
