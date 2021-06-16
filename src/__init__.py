# src/__init__.py
import os
from flask import Flask, jsonify
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy

# instantiate the app
app = Flask(__name__)
api = Api(app)

# Setting the app config
app_settings = os.environ['APP_SETTINGS']
app.config.from_object(app_settings)

# Instantiate the DB
db = SQLAlchemy(app)

# User model
class User(db.Model):
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    # Users table
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean, default=True, nullable=False)

class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }


api.add_resource(Ping, '/ping')