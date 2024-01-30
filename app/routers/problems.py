from fastapi import APIRouter, Depends, Path, Query, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from database import SessionLocal
from models import Problem
from sqlalchemy.orm import Session

router = APIRouter()

class WriteProblemBase(BaseModel):
    title : str
    description : str
    time_limit : int
    memory_limit : int
    input_format : str
    sample_input : str
    output_format : str
    sample_output : str
    constraints : str
    explanation : str | None = None

class UpdatedProblemBase(BaseModel):
    title : str | None = None
    description : str | None = None
    time_limit : int | None = None
    memory_limit : int | None = None
    input_format : str | None = None
    sample_input : str | None = None
    output_format : str | None = None
    sample_output : str | None = None
    constraints : str | None = None
    explanation : str | None = None

@router.get('/api/problems', tags=["problems"])
def read_problems():
    db = SessionLocal()
    db_problems = db.query(Problem).all()
    return db_problems
    
@router.get("/api/problems/search", tags=["problems"])
def search_problem(q : str | None = None):
    db = SessionLocal()
    items = db.query(Problem).filter(Problem.title.contains(q)).all()
    return items

@router.get('/api/problem/{problem_id}', tags=["problems"])
def read_problem(problem_id : int):
    db = SessionLocal()
    db_problem = db.query(Problem).filter(Problem.id == problem_id).first()
    return db_problem

@router.post('/api/problem', tags=["problems"])
def create_problem(new_problem : WriteProblemBase):
    db = SessionLocal()
    problem = Problem(
        title = new_problem.title,
        description = new_problem.description,
        time_limit = new_problem.time_limit,
        memory_limit = new_problem.memory_limit,
        input_format = new_problem.input_format,
        sample_input = new_problem.sample_input,
        output_format = new_problem.output_format,
        sample_output = new_problem.sample_output,
        constraints = new_problem.constraints
        )
    if new_problem.explanation is not None :
        problem.explanation = new_problem.explanation

    db.add(problem)
    db.commit()
    db.refresh(problem)
    return {"message": "Problems created successfully"}

@router.put('/api/problem/{problem_id}', tags=["problems"])
def update_problem(problem_id : int, new_problem : UpdatedProblemBase):
    db = SessionLocal()
    old_problem = db.query(Problem).filter(Problem.id == problem_id).first()
    
    if not old_problem :
        return { "message" : "No problem found"}

    if new_problem.title is not None :
        old_problem.title = new_problem.title
    
    if new_problem.description is not None :
        old_problem.description = new_problem.description
    
    if new_problem.time_limit is not None :
        old_problem.time_limit = new_problem.time_limit
    
    if new_problem.memory_limit is not None :
        old_problem.memory_limit = new_problem.memory_limit
    
    if new_problem.input_format is not None :
        old_problem.input_format = new_problem.input_format
    
    if new_problem.sample_input is not None :
        old_problem.sample_input = new_problem.sample_input
    
    if new_problem.output_format is not None :
        old_problem.output_format = new_problem.output_format
    
    if new_problem.sample_output is not None :
        old_problem.sample_output = new_problem.sample_output
    
    if new_problem.constraints is not None :
        old_problem.constraints = new_problem.constraints
    
    if new_problem.explanation is not None :
        old_problem.explanation = new_problem.explanation
    
    db.add(old_problem)
    db.commit()
    
    return { "message" : "Problem updated successfully"}

@router.delete('/api/problems/{problem_id}', tags=["problems"])
def function(problem_id : int):
    db = SessionLocal()
    problem = db.query(Problem).filter(Problem.id==problem_id).first()
    if problem is None :
        raise HTTPException(status_code=404, detail="Problem was not found")
    db.delete(problem)
    db.commit()
    
    return {"message" : "Problem deleted successfully"}
    