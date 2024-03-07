from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from models import ContestProblem, Problem
from database import SessionLocal


router = APIRouter()

class ContestProblemCreate(BaseModel):
    contest_id : int
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
    

@router.get("/contest_problems",  tags=["Contest Problem"])
def get_all_contest_problems():
    db = SessionLocal()
    contest_problems = db.query(ContestProblem).all()
    db.close()
    return contest_problems

@router.get("/contest/{contest_id}/problems", tags=["Contest Problem"])
def get_contest_problem(contest_id: int):
    db = SessionLocal()
    contest_problem = db.query(ContestProblem).filter(ContestProblem.contest_id == contest_id).all()
    db.close()
    return contest_problem

@router.post("/contest_problems", tags=["Contest Problem"])
def create_contest_problem(new_contest_problem: ContestProblemCreate):
    db = SessionLocal()

    problem = ContestProblem(
        title = new_contest_problem.title,
        contest_id = new_contest_problem.contest_id,
        description = new_contest_problem.description,
        time_limit = new_contest_problem.time_limit,
        memory_limit = new_contest_problem.memory_limit,
        input_format = new_contest_problem.input_format,
        sample_input = new_contest_problem.sample_input,
        output_format = new_contest_problem.output_format,
        sample_output = new_contest_problem.sample_output,
        constraints = new_contest_problem.constraints
        )
    
    if new_contest_problem.explanation is not None :
        problem.explanation = new_contest_problem.explanation

    db.add(problem)
    db.commit()
    db.refresh(problem)
    return {"message": "Contest Problems created successfully"}

@router.delete("/contest_problems/{contest_problem_id}", tags=["Contest Problem"])
def delete_contest_problem(contest_problem_id: int):
    db = SessionLocal()
    contest_problem = db.query(ContestProblem).filter(ContestProblem.id == contest_problem_id).all()
    if not contest_problem:
        raise HTTPException(status_code=404, detail="Contest problem not found")
    db.delete(contest_problem)
    db.commit()
    db.close()
    return {"message": "Contest problem deleted"}

@router.delete("/contest_problems/{contest_problem_id}/problems/{problem_id}", tags=["Contest Problem"])
def delete_contest_problem(contest_problem_id: int, problem_id: int):
    db = SessionLocal()
    contest_problem = db.query(ContestProblem).filter(ContestProblem.id == contest_problem_id, Problem.id == problem_id).first()
    if not contest_problem:
        raise HTTPException(status_code=404, detail="Contest problem not found")
    db.delete(contest_problem)
    db.commit()
    db.close()
    return {"message": "Contest problem deleted"}