#!/usr/bin/python2

"""
This is the flask app factory - It sets up and instance of the flask
application
"""

from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    """ Intialize Flask extensions here """

    """ Register blueprints here """

    @app.route('/test/')
    def test_page():
        return '<h1> Testing the flask app factory pattern</h1>'

    return app
