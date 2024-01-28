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

class Problem(Base):
    __tablename__ = "problems"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255))
    description = Column(String)
    time_limit = Column(Integer)
    memory_limit = Column(Integer)
    input_format = Column(String)
    sample_input = Column(String)
    output_format = Column(String)
    sample_output = Column(String)
    constraints = Column(String)
    explanation = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    