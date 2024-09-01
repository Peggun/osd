from flask import Blueprint, render_template

api = Blueprint("api", __name__)

@api.route("/api")
def api_page():
    return render_template("api_page/html/html-api-page.html")