from flask import Flask
from config import DevelopmentConfig
from db.db import db  # Import here to avoid circular import issues

# Import routes after creating the Flask app
def create_app():  # Create the app and register routes
    app = Flask(__name__, static_folder="static", template_folder="templates")

    app.config.from_object(DevelopmentConfig)

    # Register blueprints
    from .routes.home_page.home_route import home as home_blueprint
    from .routes.documentation_page.documentation_route import docs as docs_blueprint
    from .routes.api_page.api_page_route import api as api_blueprint
    from .routes.community_page.community_route import community as community_blueprint
    from .routes.database_page.database_route import database as database_blueprint

    app.register_blueprint(home_blueprint)
    app.register_blueprint(docs_blueprint)
    app.register_blueprint(api_blueprint)
    app.register_blueprint(community_blueprint)
    app.register_blueprint(database_blueprint)

    from db.initdb import init_db
    init_db(app)  # Call the initialization function

    return app, db