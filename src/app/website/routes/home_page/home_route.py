from flask import Blueprint,  render_template

home = Blueprint('home', __name__)

@home.route('/home')
def home_page():

    return "Hello there again"