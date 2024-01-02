from flask import Blueprint, g
from src.model.User import User
from src.schema.UserSchema import UserSchema

bp = Blueprint('users', __name__, url_prefix='/api')

@bp.get('/users')
def get_users():
    return 'hello'


