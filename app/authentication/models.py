from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin

from app import db, login_manager


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return self.name


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), nullable=False, unique=True, index=True)
    password_hash = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return self.username

    @property
    def password(self):
        raise AttributeError('Password is not readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


class Extra(db.Model):
    __tablename__ = 'extras'
    id = db.Column(db.Integer, primary_key=True)
    attr = db.Column(db.String(30))
    string_value = db.Column(db.String(255))
    integer_value = db.Column(db.Integer)
    date_value = db.Column(db.DateTime())
