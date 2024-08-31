from flask import Flask, make_response, request
from config import Config, DevelopmentConfig, ProductionConfig

from .routes.home_page.home_route import home as home_blueprint
from .routes.documentation_page.documentation_route import docs as docs_blueprint

app = Flask(__name__, static_folder="static", template_folder="templates")


def create_app():  # Creates the app for run.py to start.

    from db.initdb import (
        init_db,
    )  # This stops the circular import from happening

    app.register_blueprint(home_blueprint)
    app.register_blueprint(docs_blueprint)

    app.config.from_object(DevelopmentConfig)

    db = init_db()

    return app, db
