from sqlalchemy import String, Integer, DateTime, Column, ForeignKey
from sqlalchemy.orm import mapped_column
from flask import g
from sqlalchemy.sql import func
class Post(g.base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = mapped_column(ForeignKey('users.id'))
    sender_id = mapped_column(ForeignKey('users.id'))
    message = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

