from flask import g
from sqlalchemy import String, Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func

class GroupFollower(g.base):
    __tablename__ = 'group_followers'
    id = Column(Integer, primary_key=True)
    group_id = mapped_column(ForeignKey('groups.id'))
    user_id = mapped_column(ForeignKey('users.id'))
    typed = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())