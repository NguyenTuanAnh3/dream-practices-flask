from flask import jsonify

from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required

from src.repository.authRepository import AuthRepository
from src.exception.authException import EmailExists

class AuthService():

    def __init__(self):
        self.authRepo = AuthRepository()

    def register(self, email, password):
        try:
            self.authRepo.register(email=email, password=password)
        except EmailExists as e:
            return jsonify({"msg":e.message}), 400
        else:
            access_token = create_access_token(identity=email)
            return jsonify(access_token=access_token)