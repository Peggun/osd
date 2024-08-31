from flask import Blueprint, render_template, redirect, url_for, make_response, request

home = Blueprint("home", __name__)


# Redirect to the home page.
@home.route("/")
def redirect_to_home():
    return redirect(url_for("home.home_page"))


# Home page route.
@home.route("/home")
def home_page():
    # Check if the 'visited' cookie is set.
    visited = request.cookies.get("visited")

    # If the cookie is not set, display the 'Get Started' button.
    show_get_started = not visited

    return render_template(
        "home_page/html/html-home.html", show_get_started=show_get_started
    )


# Route that the "Get Started" button will link to.
@home.route("/get-started")
def get_started():
    # Create a response object.
    response = make_response(redirect(url_for("home.home_page")))

    # Set the 'visited' cookie to 'true' with an expiration of 30 days.
    response.set_cookie("visited", "true", max_age=30 * 24 * 60 * 60)

    return response


@home.route("/delete_cookie")
def delete_cookie():
    response = make_response(redirect(url_for("home.home_page")))
    response.set_cookie("visited", "", expires=0)
    return response


@home.route("/set_visited_cookie")
def set_visited_cookie():
    response = make_response({"status": "success"})
    response.set_cookie(
        "visited", "true", max_age=60 * 60 * 24 * 365
    )  # 1 year duration
    return response
