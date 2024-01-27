from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base

class User(Base):
    __tablename__ = "users"
    
    id=Column(Integer, primary_key=True)
    name=Column(String)
    nim=Column(String)
    score=Column(Integer)
    password=Column(String)
    email= Column(String, unique=True, index=True)
    email_verified_at = Column(DateTime, default=None)
    remember_token = Column(String, default=None)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    