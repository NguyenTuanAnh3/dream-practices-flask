from src.model.User import User
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError
from app.config import db
from src.exception.authException import EmailExists

class AuthRepository():
    def __init__(self):
        self.dbs = db.init_db()

    def register(self, email, password):
        try:
            user = User(email=email, password=generate_password_hash(password))
            self.dbs.add(user)
            self.dbs.commit()
        except IntegrityError:
            self.dbs.rollback()
            raise EmailExists