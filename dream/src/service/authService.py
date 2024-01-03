from flask import jsonify
from werkzeug.security import check_password_hash

from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import set_access_cookies

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
            response = jsonify({"msg":"registered successful"})
            access_token = create_access_token(identity=email)
            set_access_cookies(response, access_token)
            return response, 200

    def login(self, email, password):
        user = self.authRepo.login(email=email)

        if user is None:
            return jsonify({"msg": "Email not found"}), 404
        elif not check_password_hash(user.password, password):
            return jsonify({"msg":"Incorrect Password"}), 401

        response = jsonify({"msg": "Login successful"})
        access_token = create_access_token(identity=user.email)
        set_access_cookies(response, access_token)
        return response, 200
