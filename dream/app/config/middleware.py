from flask_jwt_extended import JWTManager

def manage_jwt(app):
    JWTManager(app)
