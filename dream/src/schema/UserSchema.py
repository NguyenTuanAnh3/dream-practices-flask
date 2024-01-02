from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from src.model.User import User

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        fields = ['first_name','middle_name', 'last_name', 'mobile', 'email', 'password', 'registered_at', 'last_login', 'intro', 'profile']