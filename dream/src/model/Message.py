from flask import g
from sqlalchemy import Column, ForeignKey, String, Integer, DateTime
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func

class Message(g.base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    source_id = mapped_column(ForeignKey('users.id'))
    target_id = mapped_column(ForeignKey('users.id'))
    message = Column(String, nullable=True)
    create_at = Column(DateTime(timezone=True), server_default=func.now())
    update_at = Column(DateTime(timezone=True), onupdate=func.now())