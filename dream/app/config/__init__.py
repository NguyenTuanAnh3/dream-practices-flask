import os
from flask import Flask, jsonify
from app.config import db
from app.config import middleware

def create_app(test_config=None):
    app = Flask('dream', instance_path=f'{os.path.dirname(os.path.dirname(__file__))}/instance', instance_relative_config=True)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:

        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    with app.app_context():
        db.init_app(app)
        middleware.manage_jwt(app)

    from src.api import user
    from src import auth

    app.register_blueprint(auth.bp)
    app.register_blueprint(user.bp)

    return app
