from flask import Blueprint, render_template

community = Blueprint("community", __name__)

@community.route("/community")
def community_page():
    return render_template("community_page/html/html-community-page.html")