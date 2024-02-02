from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class User(Base):
    __tablename__ = "users"
    
    id=Column(String(255), primary_key=True)
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
    # user_id = Column(String(255), ForeignKey("users.id"))
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
    categories = relationship("Category", secondary="problem_categories")

    
class Language(Base):
    __tablename__ ="languages"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


class Submission(Base):
    __tablename__ = "submissions"
    
    id = Column(Integer, primary_key=True, index= True, autoincrement=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    problem_id = Column(Integer, ForeignKey("problems.id"))
    language_id = Column(Integer, ForeignKey("languages.id"))
    status = Column(String)
    time = Column(Integer)
    memory = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    

class TestCase(Base):
    __tablename__ = "test_cases"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    problem_id = Column(Integer, ForeignKey("problems.id"))
    input = Column(String)
    output = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

# class TestCaseResult(Base):
#     __tablename__ = "test_cases_results"
    
    
class Admin(Base):
    __tablename__ = "admins"
    
    id =  Column(String(255), primary_key=True)
    user_id = Column(String(255), ForeignKey("users.id"))
    role = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)


class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    
    
    
class ProblemCategory(Base):
    __tablename__ = "problem_categories"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    category_id = Column(String, ForeignKey("categories.id"))
    problem_id = Column(Integer, ForeignKey("problems.id"))
    
class Contest(Base):
    __tablename__ = "contests" 
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    admin_id = Column(String, ForeignKey('users.id'))
    title = Column(String)
    slug = Column(String)
    description = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    
    
    
