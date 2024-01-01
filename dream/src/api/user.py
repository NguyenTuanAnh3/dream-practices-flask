from flask import Blueprint, g
from src.model.User import User
from src.schema.UserSchema import UserSchema

bp = Blueprint('users', __name__, url_prefix='/api/')

@bp.get('/users')
def get_users():
    users = User.query.all()
    user_schema = UserSchema(many=True)
    return user_schema.dump(users)


