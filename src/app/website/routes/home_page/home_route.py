from flask import Blueprint,  render_template, redirect, url_for

home = Blueprint('home', __name__)

@home.route('/')
def redirect_to_home():
    return redirect(url_for('home.home_page'))

@home.route('/home')
def home_page():
    return "Hello there again"

@home.route('/test')
def test_page():
    return "This is a test"