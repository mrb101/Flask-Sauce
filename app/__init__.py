from flask import Flask, render_template
from flask.ext.moment import Moment
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from config import config


moment = Moment()
mail = Mail()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    moment.init_app(app)
    mail.init_app(app)
    db.init_app(app)

    # routes and custom error pages

    from authentication import authentication as authentication_blueprint
    app.register_blueprint(authentication_blueprint)

    return app
