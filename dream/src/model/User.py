from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from flask import g

class User(g.base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=True)
    middle_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    mobile = Column(String(50), nullable= True)
    email = Column(String(120), unique=True)
    password = Column(String(120))
    registered_at = Column(DateTime(timezone=True), server_default=func.now())
    last_login = Column(DateTime, nullable=True)
    intro = Column(String, nullable=True)
    profile = Column(String, nullable=True)

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}'
