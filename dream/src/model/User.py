from sqlalchemy import Column, Integer, String
from flask import g

class User(g.base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(120))

    def __init__(self, name=None, email=None, password = None):
        self.name = name
        self.email = email
        self.password = password
