from flask import jsonify, request
from functools import wraps

def validateAuth(func):
    @wraps(func)
    def handleValidation(*args, **kwargs):
        email = request.json.get("email", None)
        password = request.json.get("password", None)
        if email is None and password is None:
            return jsonify({'msg': "Please enter email and password"}), 401
        if email is None:
            return jsonify({'msg': "Email is required"}), 401
        if password is None:
            return jsonify({"msg": "Password is required"}), 401
        return func(email=email, password=password)
    return handleValidation
