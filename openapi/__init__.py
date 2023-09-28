import os
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask import Flask, session
from openapi.config import App_Config
from flask_cors import CORS

# Create an instance of Swagger

db = SQLAlchemy()




def create_app():
    """
    Create a new instance of the app with the given configuration.

    :param config_class: configuration class
    :return: app
    """
    # Initialize Flask-
    app = Flask(__name__)
    
    # Initialize CORS
    CORS(app, supports_credentials=True)


    # Initialize SQLAlchemy
    db.init_app(app)





    # create db tables from models if not exists
    with app.app_context():
        db.create_all()

    return app