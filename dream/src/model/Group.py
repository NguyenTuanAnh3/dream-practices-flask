from flask import g
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func

class Group(g.base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    created_by = mapped_column(ForeignKey('users.id'))
    updated_by = mapped_column(ForeignKey('users.id'))
    title = Column(String, nullable=False)
    metaTitle = Column(String, nullable=False)
    slug = Column(String(100), nullable=False)
    summary = Column(String, nullable=True)
    status = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    profile = Column(String, nullable=True)
    content =  Column(String, nullable=True)