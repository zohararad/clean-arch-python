from flask import Flask
from .api import blueprint


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')
    app.register_blueprint(blueprint)
    return app
