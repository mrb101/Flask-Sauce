from flask import Blueprint

resturants = Blueprint('resturants', __name__)

from . import views
