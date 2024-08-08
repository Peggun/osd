from flask import Flask
from config import Config, DevelopmentConfig, ProductionConfig

app = Flask(__name__,static_folder='static',template_folder='templates') # For all routes otherwise app is None



def create_app():

    from .routes.home_page.home_route import home as home_blueprint

    app.register_blueprint(home_blueprint)

    app.config.from_object(DevelopmentConfig)

    return app