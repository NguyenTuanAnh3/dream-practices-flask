from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import mapped_column
from flask import g
from sqlalchemy.sql import func

class GroupPost(g.base):
    __tablename__ = 'group_posts'
    id = Column(Integer, primary_key=True)
    group_id = mapped_column(ForeignKey('groups.id'))
    user_id = mapped_column(ForeignKey('users.id'))
    message = Column(String, nullable=True)
    create_at = Column(DateTime(timezone=True), server_default=func.now())
    update_at = Column(DateTime(timezone=True), onupdate=func.now())