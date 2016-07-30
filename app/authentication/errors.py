from flask import render_tamplate
from . import authentication


@authentication.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
