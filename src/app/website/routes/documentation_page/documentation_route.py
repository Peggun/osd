from flask import Blueprint, render_template, redirect, url_for, make_response, request

docs = Blueprint("docs", __name__)


@docs.route("/docs")
def docs_page():
    return render_template("documentation_page/html/html-documentation.html")


@docs.route("/docs/getting-started")
def docs_getting_started():
    return render_template("documentation_page/html/html-docs-getting-started.html")


@docs.route("/docs/api-reference")
def docs_api_reference():
    return render_template("documentation_page/html/html-docs-api-reference.html")  


@docs.route("/contributing")
def docs_contributing():
    return "Contributing"
