from flask import render_template
from . import authentication

@authentication.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('authentication/login.html')


@authentication.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('authentication/register.html')
