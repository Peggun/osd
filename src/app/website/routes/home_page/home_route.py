from src.app.website import app

from flask import Blueprint

home = Blueprint('home', __name__)

@home.route('/home')
def home_page():
    return "Hello there again"