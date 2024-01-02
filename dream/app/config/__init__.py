import os
from flask import Flask, jsonify
from app.config import db

def create_app(test_config=None):
    app = Flask(__name__, instance_path=f'{os.path.dirname(os.path.dirname(__file__))}/instance', instance_relative_config=True)

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

    from src.api import user
    app.register_blueprint(user.bp)

    return app
