import json
from flask import Flask, jsonify
from app.config.config import DatabaseConfig
from app.config import db

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(DatabaseConfig)

    with app.app_context():
        db.init_app(app)

    from src.api import user
    app.register_blueprint(user.bp)

    return app
