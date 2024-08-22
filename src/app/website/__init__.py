from flask import Flask
from config import Config, DevelopmentConfig, ProductionConfig
import sentry_sdk
import os

from .routes.home_page.home_route import home as home_blueprint

app = Flask(__name__, static_folder="static", template_folder="templates")


def create_app():  # Creates the app for run.py to start.

    from db.initdb import (
        init_db,
        books_db_path,
    )  # This stops the circular import from happening

    app.register_blueprint(home_blueprint)
    app.config.from_object(DevelopmentConfig)

    db = init_db()

    return app, db
