from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from src.model.User import User

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

    id = auto_field()
    name = auto_field()
    email = auto_field()
    password = auto_field()