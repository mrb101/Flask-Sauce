from flask import render_template
from . import main


@main.route('/', methods=['GET'])
def index():
    return render_template('main/index.html')


@main.route('/', methods=['GET'])
def about():
    return render_template('main/about.html')


@main.route('/', methods=['GET'])
def contact():
    return render_template('main/contact.html')
