from flask import Blueprint, jsonify, request

from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required

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
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

@bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200