from flask import g
from sqlalchemy import String, Integer, DateTime, ForeignKey, Column
from sqlalchemy.orm import mapped_column

class GroupMeta(g.base):
    __tablename__ = 'group_metas'
    id = Column(Integer, primary_key=True)
    group_id = mapped_column(ForeignKey('groups.id'))
    key = Column(String)
    content = Column(String, nullable=True)
