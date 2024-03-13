from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..models import ContestProblem, Problem, Contest
from ..database import SessionLocal
from sqlalchemy.orm import Session, joinedload
from fastapi import Depends
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
    category : list[int] | None = None    
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    

@router.get("/api/contest/problems/all",  tags=["Contest Problem"])
def get_all_contest_problems(db: Session = Depends(get_db)):
    contest_problems = db.query(ContestProblem).all()
    if not contest_problems:
        raise HTTPException(status_code=404, detail="Contest Problems Not Found")
    return {"status" : "ok","data" : contest_problems}

@router.get("/api/contest/{contest_id}/problems", tags=["Contest Problem"])
def contest_problems(contest_id: int, db: Session = Depends(get_db)):
    db_contest = db.query(Contest).filter(Contest.id == contest_id).first()
    if db_contest is None:
        raise HTTPException(status_code=404, detail="Contest Not Found")
    db_contest_problems = (
        db.query(ContestProblem)
        .filter(ContestProblem.contest_id == contest_id)
        .options(joinedload(ContestProblem.categories))
        .all()
    )

    return db_contest_problems


@router.post("/api/contest/problem", tags=["Contest Problem"])
def create_contest_problem(new_contest_problem: ContestProblemCreate, db: Session = Depends(get_db)):

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
    return {"message": "Contest Problems created successfully", "data" : problem}

@router.put("/api/contest/problems/{contest_problem_id}", tags=["Contest Problem"])
def update_contest_problem(contest_problem_id: int, new_contest_problem: ContestProblemCreate, db: Session = Depends(get_db)):
    contest_problem = db.query(ContestProblem).filter(ContestProblem.id == contest_problem_id).first()
    if not contest_problem:
        raise HTTPException(status_code=404, detail="Contest problem not found")
    contest_problem.title = new_contest_problem.title
    contest_problem.description = new_contest_problem.description
    contest_problem.time_limit = new_contest_problem.time_limit
    contest_problem.memory_limit = new_contest_problem.memory_limit
    contest_problem.input_format = new_contest_problem.input_format
    contest_problem.sample_input = new_contest_problem.sample_input
    contest_problem.output_format = new_contest_problem.output_format
    contest_problem.sample_output = new_contest_problem.sample_output
    contest_problem.constraints = new_contest_problem.constraints
    contest_problem.explanation = new_contest_problem.explanation
    db.commit()
    db.refresh(contest_problem)
    db.close()
    return {"message": "Contest problem updated", "data": contest_problem}

@router.delete("/api/contest/problems/{contest_problem_id}", tags=["Contest Problem"])
def delete_contest_problem(contest_problem_id: int, db: Session = Depends(get_db)):
    contest_problem = db.query(ContestProblem).filter(ContestProblem.id == contest_problem_id).all()
    if not contest_problem:
        raise HTTPException(status_code=404, detail="Contest problem not found")
    db.delete(contest_problem)
    db.commit()
    db.close()
    return {"message": "Contest problem deleted"}


@router.delete("/api/contest/problems/{contest_problem_id}/problems/{problem_id}", tags=["Contest Problem"])
def delete_contest_problem(contest_problem_id: int, problem_id: int, db: Session = Depends(get_db)):
    contest_problem = db.query(ContestProblem).filter(ContestProblem.id == contest_problem_id, Problem.id == problem_id).first()
    if not contest_problem:
        raise HTTPException(status_code=404, detail="Contest problem not found")
    db.delete(contest_problem)
    db.commit()
    db.close()
    return {"message": "Contest problem deleted"}