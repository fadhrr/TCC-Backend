from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from database import Base


class User(Base):
    __tablename__ = "users"
    
    id=Column(String(255), primary_key=True)
    name=Column(String)
    nim=Column(String)
    score=Column(Integer)
    email= Column(String, unique=True, index=True)
    email_verified_at = Column(DateTime, default=None)
    remember_token = Column(String, default=None)
    created_at = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=7))
    updated_at = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=7))


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
    created_at = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=7))
    updated_at = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=7))
    categories = relationship("Category", secondary="problem_categories", back_populates="problems")

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    problems = relationship("Problem", secondary="problem_categories", back_populates="categories")
    local_problems = relationship("LocalProblem", secondary="local_problem_categories", back_populates="categories")
    contest_problems = relationship("ContestProblem",secondary="contest_problem_categories", back_populates="categories")
    
    
class ProblemCategory(Base):
    __tablename__ = "problem_categories"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    problem_id = Column(Integer, ForeignKey("problems.id"))
    
    
class Language(Base):
    __tablename__ ="languages"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    created_at = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=7))


class Submission(Base):
    __tablename__ = "submissions"
    
    id = Column(Integer, primary_key=True, index= True, autoincrement=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    problem_id = Column(Integer, ForeignKey("problems.id"))
    language_id = Column(Integer, ForeignKey("languages.id"))
    status = Column(String, default=None)
    time = Column(Float)
    memory = Column(Integer)
    code = Column(String, default="")
    created_at = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=7))
    
    
    
    

class TestCase(Base):
    __tablename__ = "test_cases"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    problem_id = Column(Integer, ForeignKey("problems.id"))
    input = Column(String)
    output = Column(String)
    created_at = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=7))
    updated_at = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=7))

class TestCaseResult(Base):
    __tablename__ = "test_case_results"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    submission_id = Column(Integer, ForeignKey("submissions.id"))
    status = Column(String, default=None)
    time = Column(Float, default=None)
    memory = Column(Integer, default=None)
    created_at = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=7))
    

class Admin(Base):
    __tablename__ = "admins"
    
    id =  Column(String(255), primary_key=True)
    user_id = Column(String(255), ForeignKey("users.id"))
    role = Column(Integer)
    created_at = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=7))
    updated_at = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=7))

class Contest(Base):
    __tablename__ = "contests" 
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    admin_id = Column(String, ForeignKey('users.id'))
    title = Column(String)
    slug = Column(String)
    description = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    created_at = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=7))
    
class ContestParticipant(Base):
    __tablename__ = "contest_participants"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(String, ForeignKey("users.id"))
    contest_id = Column(Integer, ForeignKey("contests.id"))
    
class ContestProblem(Base):
    __tablename__ = "contest_problems"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    contest_id = Column(Integer, ForeignKey("contests.id"))
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
    created_at = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=7))
    updated_at = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=7))
    categories = relationship("Category", secondary="contest_problem_categories", back_populates="contest_problems")
    

class ContestProblemCategory(Base):
    __tablename__ = "contest_problem_categories"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    contest_problem_id = Column(Integer, ForeignKey("contest_problems.id"))
    
class ContestSubmission(Base):
    __tablename__ = "contest_submissions"
    
    id = Column(Integer, primary_key=True, index= True, autoincrement=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    contest_id = Column(Integer, ForeignKey("contests.id"))
    problem_id = Column(Integer, ForeignKey("contest_problems.id"))
    language_id = Column(Integer, ForeignKey("languages.id"))
    status = Column(String, default=None)
    time = Column(Float)
    memory = Column(Integer)
    code = Column(String, default="")
    created_at = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=7))
    
    
    # ??
class ContestTestCase(Base):
    __tablename__ = "contest_test_cases"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    problem_id = Column(Integer, ForeignKey("contest_problems.id"))
    input = Column(String)
    output = Column(String)
    created_at = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=7))
    updated_at = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=7))

class ContestTestCaseResult(Base):
    __tablename__ = "contest_test_case_results"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    submission_id = Column(Integer, ForeignKey("contest_submissions.id"))
    status = Column(String, default=None)
    time = Column(Float, default=None)
    memory = Column(Integer, default=None)
    created_at = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=7))

class Notification(Base):
    __tablename__ = "notifications"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    contest_id = Column(String, ForeignKey("contest.id"))
    title = Column(String)
    description = Column(String)
    created_at = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=7))
    updated_at = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=7))
    
################## LOCAL ######################

class LocalContest(Base):
    __tablename__ = "local_contests"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    admin_id = Column(String, ForeignKey('users.id'))
    title = Column(String)
    slug = Column(String)
    description = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    created_at = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=7))
    
class LocalContestParticipant(Base):
    __tablename__ = "local_contest_participants"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    contest_id = Column(Integer, ForeignKey("local_contests.id"))
    user_id = Column(String, ForeignKey("users.id"))

class LocalContestProblem(Base):
    __tablename__ = "local_contest_problems"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    contest_id = Column(Integer, ForeignKey("local_contests.id"))
    problem_id = Column(Integer, ForeignKey("problems.id"))

class LocalProblem(Base):
    __tablename__ = "local_problems"
    
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
    created_at = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=7))
    updated_at = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=7))
    categories = relationship("Category", secondary="local_problem_categories", back_populates="local_problems")

class LocalSubmission(Base):
    __tablename__ = "local_submissions"
    
    id = Column(Integer, primary_key=True, index= True, autoincrement=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    problem_id = Column(Integer, ForeignKey("local_problems.id"))
    language_id = Column(Integer, ForeignKey("languages.id"))
    status = Column(String, default=None)
    time = Column(Float)
    memory = Column(Integer)
    code = Column(String, default="")
    created_at = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=7))

class LocalTestCase(Base):
    __tablename__ = "local_test_cases"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    problem_id = Column(Integer, ForeignKey("local_problems.id"))
    input = Column(String)
    output = Column(String)
    created_at = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=7))
    updated_at = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=7))

class LocalTestCaseResult(Base):
    __tablename__ = "local_test_case_results"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    submission_id = Column(Integer, ForeignKey("local_submissions.id"))
    status = Column(String, default=None)
    time = Column(Float, default=None)
    memory = Column(Integer, default=None)
    created_at = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=7))


class LocalProblemCategory(Base):
    __tablename__ = "local_problem_categories"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    category_id = Column(String, ForeignKey("categories.id"))
    problem_id = Column(Integer, ForeignKey("local_problems.id"))
    



