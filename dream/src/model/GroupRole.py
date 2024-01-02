from flask import g
from sqlalchemy import String, DateTime, Integer, Column

class GroupRole(g.base):
    __tablename__ = 'group_roles'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable= False)
    description = Column(String, nullable=True)