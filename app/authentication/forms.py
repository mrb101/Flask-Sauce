from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, EqualTo


class RegisterForm(Form):
    name = StringField('Full Name', validators=[Required(), Length(1, 255)])
    email = StringField('Email',
        validators=[Required(), Length(1, 255), Email()])
    username = StringField('User Name', validators=[Required(), Length(1, 64)])
    password = PasswordField('Password', validators=[
                Required(), EqualTo('password2', message='Passwords must match')
    ])
    password2 = PasswordField('Confirm password', validators=[Required()])


class LoginForm(Form):
    username = StringField('User Name', validators=[Required(), Length(1, 64)])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Sign In')
