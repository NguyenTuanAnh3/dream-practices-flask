from flask import g
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func

class GroupMember(g.base):
    __tablename__ = 'group_members'
    id = Column(Integer, primary_key=True)
    group_id = mapped_column(ForeignKey('groups.id'))
    user_id = mapped_column(ForeignKey('users.id'))
    role_id = mapped_column(ForeignKey('group_roles.id'))
    status = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    notes = Column(String, nullable=True)