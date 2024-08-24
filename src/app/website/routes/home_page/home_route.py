from flask import Blueprint, render_template, redirect, url_for

import pyhtmlify.HTMLTags.tags as tags

home = Blueprint("home", __name__)

# Just routes for the home page.l 

@home.route("/")
def redirect_to_home():
    return redirect(url_for("home.home_page"))


@home.route("/home")
def home_page():
    return render_template("home_page/html/html-home.html")