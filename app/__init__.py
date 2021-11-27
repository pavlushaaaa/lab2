from flask import Flask
from flask_restful import Api

api = Api()


def create_app():
    from .resources.routes import initialize_routes
    app = Flask(__name__)
    initialize_routes(api)
    api.init_app(app)
    return app
