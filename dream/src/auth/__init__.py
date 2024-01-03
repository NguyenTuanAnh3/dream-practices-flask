from flask import Blueprint, jsonify, request

from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import unset_jwt_cookies

from src.validator import authValidator as av
from src.service.authService import AuthService

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.post("/register")
@av.validateAuth
def register(*args, **kwargs):
    email, password = kwargs['email'], kwargs['password']
    authService = AuthService()
    result = authService.register(email=email, password=password)
    return result


@bp.post("/login")
@av.validateAuth
def login(*args, **kwargs):
    email, password = kwargs['email'], kwargs['password']
    authService = AuthService()
    result = authService.login(email=email, password=password)
    return result

@bp.get("/logout")
@jwt_required()
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response, 200
