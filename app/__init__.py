from flask import Flask, render_template

from flask.ext.moment import Moment
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

from config import config


moment = Moment()
mail = Mail()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'authentication.login'

from app.authentication import models

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    config[config_name].init_app(app)

    # register extensions

    moment.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # register blueprints

    from authentication import authentication as authentication_blueprint
    app.register_blueprint(authentication_blueprint)

    from customers import customers as customers_blueprint
    app.register_blueprint(customers_blueprint)

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from orders import orders as orders_blueprint
    app.register_blueprint(orders_blueprint)

    from resturants import resturants as resturants_blueprint
    app.register_blueprint(resturants_blueprint)

    return app
