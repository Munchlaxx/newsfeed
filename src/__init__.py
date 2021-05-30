# src/__init__.py
from flask import Flask, jsonify
from flask_restx import Resource, Api
from .config import DevelopmentConfig


# instantiate the app
app = Flask(__name__)

api = Api(app)

# Setting the app config
app.config.from_object(DevelopmentConfig)


class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }


api.add_resource(Ping, '/ping')