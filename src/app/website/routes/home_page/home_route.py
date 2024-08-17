from flask import Blueprint,  render_template

home = Blueprint('home', __name__)

@home.route('/home')
def home_page():
    1/0
    return "Hello there again"

@home.route('/test')
def test_page():
    1/0
    return "This is a test"