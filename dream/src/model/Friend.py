from sqlalchemy import Column, Integer, String, DateTime , ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func
from flask import g

class Friend(g.base):
    __tablename__ = 'friends'
    id = Column(Integer, primary_key=True)
    source_id = mapped_column(ForeignKey('users.id'))
    target_id = mapped_column(ForeignKey('users.id'))
    typed = Column(Integer, default=0)
    status = Column(Integer, default=0)
    create_at = Column(DateTime(timezone=True), server_default=func.now())
    update_at = Column(DateTime(timezone=True), onupdate=func.now())
    notes = Column(String, nullable=True)
