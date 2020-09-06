#!/bin/env python
from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()


def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'CHANGE_LATER'

    from .mod_test import mod_test as test
    app.register_blueprint(test)


    socketio.init_app(app)
    return app

