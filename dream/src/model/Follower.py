from flask import g
from sqlalchemy import Integer, String, ForeignKey, Column, DateTime
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func

class Follower(g.base):
    __tablename__= 'followers'
    id = Column(Integer, primary_key=True)
    source_id = mapped_column(ForeignKey('users.id'))
    target_id = mapped_column(ForeignKey('users.id'))
    typed = Column(Integer, default=0)
    create_at = Column(DateTime(timezone=True), server_default=func.now())
    update_at = Column(DateTime(timezone=True), onupdate=func.now())
