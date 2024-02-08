from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from models import ContestProblem, Problem
from database import SessionLocal

router = APIRouter()

class ContestProblemCreate(BaseModel):
    contest_id: int
    problem_id: int

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
def create_contest_problem(contest_problem: ContestProblemCreate):
    db = SessionLocal()

    contest_problem = ContestProblem(contest_id=contest_problem.contest_id, problem_id=contest_problem.problem_id)
    db.add(contest_problem)
    db.commit()
    db.refresh(contest_problem)
    db.close()
    return contest_problem

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