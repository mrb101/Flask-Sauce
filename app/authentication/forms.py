from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email


class RegisterForm(Form):
    name = StringField('Full Name', validators=[Required(), Length(1, 255)])
    email = StringField('Email',
        validators=[Required(), Length(1, 255), Email()])
    username = StringField('User Name', validators=[Required(), Length(1, 64)])


class LoginForm(Form):
    username = StringField('User Name', validators=[Required(), Length(1, 64)])
    password = PasswordField('Password', validators=[required()])
    submit = SubmitField('Sign In')
