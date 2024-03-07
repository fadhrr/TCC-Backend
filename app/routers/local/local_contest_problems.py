from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ...models import LocalContestProblem, LocalProblem
from ...database import SessionLocal

router = APIRouter()

class LocalContestProblemCreate(BaseModel):
    contest_id: int
    problem_id: int

@router.get("/local_contest_problems", tags=["Local Contest Problem"])
def get_all_contest_problems():
    db = SessionLocal()
    contest_problems = db.query(LocalContestProblem).all()
    db.close()
    return contest_problems

@router.get("/local_contest/{contest_id}/problems", tags=["Local Contest Problem"])
def get_contest_problem(contest_id: int):
    db = SessionLocal()
    contest_problem = db.query(LocalContestProblem).filter(LocalContestProblem.contest_id == contest_id).all()
    db.close()
    return contest_problem

@router.post("/local_contest_problems", tags=["Local Contest Problem"])
def create_contest_problem(contest_problem: LocalContestProblemCreate):
    db = SessionLocal()

    contest_problem = LocalContestProblem(contest_id=contest_problem.contest_id, problem_id=contest_problem.problem_id)
    db.add(contest_problem)
    db.commit()
    db.refresh(contest_problem)
    db.close()
    return contest_problem

@router.delete("/local_contest_problems/{contest_problem_id}", tags=["Local Contest Problem"])
def delete_contest_problem(contest_problem_id: int):
    db = SessionLocal()
    contest_problem = db.query(LocalContestProblem).filter(LocalContestProblem.id == contest_problem_id).all()
    if not contest_problem:
        raise HTTPException(status_code=404, detail="Contest problem not found")
    db.delete(contest_problem)
    db.commit()
    db.close()
    return {"message": "Contest problem deleted"}

@router.delete("/local_contest_problems/{contest_problem_id}/problems/{problem_id}", tags=["Local Contest Problem"])
def delete_contest_problem(contest_problem_id: int, problem_id: int):
    db = SessionLocal()
    contest_problem = db.query(LocalContestProblem).filter(LocalContestProblem.id == contest_problem_id, LocalProblem.id == problem_id).first()
    if not contest_problem:
        raise HTTPException(status_code=404, detail="Contest problem not found")
    db.delete(contest_problem)
    db.commit()
    db.close()
    return {"message": "Contest problem deleted"}