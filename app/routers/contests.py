from fastapi import APIRouter, HTTPException
from database import SessionLocal
from models import Contest, ContestProblem, ContestProblemCategory, Category, ContestParticipant, User, ContestSubmission
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import Depends

## Untuk Loggin
# import logging

# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class WriteContestBase(BaseModel):
    admin_id: str
    title: str
    slug: str
    description: str | None = None
    start_time: datetime
    end_time: datetime


class UpdateContestBase(BaseModel):
    title: str | None = None
    slug: str | None = None
    description: str | None = None
    start_time: datetime | None = None
    end_time: datetime | None = None


@router.get("/api/contests", tags=["Contest"])
def read_all_contests(db: Session = Depends(get_db)):

    db_contests = db.query(Contest).all()
    return db_contests


@router.get("/api/contest/{contest_id}", tags=["Contest"])
def read_contest(contest_id: int, db: Session = Depends(get_db)):

    db_contest = db.query(Contest).filter(Contest.id == contest_id).first()
    if db_contest is None:
        raise HTTPException(status_code=404, detail="Contest Not Found")
    return db_contest


@router.post("/api/contest", tags=["Contest"])
def write_contest(new_contest: WriteContestBase, db: Session = Depends(get_db)):

    new_db_contest = Contest(
        admin_id=new_contest.admin_id,
        title=new_contest.title,
        slug=new_contest.slug,
        description=new_contest.description,
        start_time=new_contest.start_time,
        end_time=new_contest.end_time,
    )
    db.add(new_db_contest)
    db.commit()
    db.refresh(new_db_contest)
    return {"message": "Contest created successfully"}


@router.put("/api/contest/{contest_id}", tags=["Contest"])
def update_contest(
    contest_id: int, updated_contest: UpdateContestBase, db: Session = Depends(get_db)
):

    new_updated_contest = db.query(Contest).filter(Contest.id == contest_id).first()
    if new_updated_contest is None:
        raise HTTPException(status_code=404, detail="Contest Not Found")

    if updated_contest.title is not None:
        new_updated_contest.title = updated_contest.title

    if updated_contest.slug is not None:
        new_updated_contest.slug = updated_contest.slug

    if updated_contest.description is not None:
        new_updated_contest.description = updated_contest.description

    if updated_contest.start_time is not None:
        new_updated_contest.start_time = updated_contest.start_time

    if updated_contest.end_time is not None:
        new_updated_contest.end_time = updated_contest.end_time

    db.add(new_updated_contest)
    db.commit()
    db.refresh(new_updated_contest)

    return {"message": "Contest updated succesfully"}


@router.delete("/api/contest/{contest_id}", tags=["Contest"])
def delete_contest(contest_id: int, db: Session = Depends(get_db)):

    db_contest = db.query(Contest).filter(Contest.id == contest_id).first()
    db.delete(db_contest)
    db.commit()
    return {"message": "Contest deleted succesfully"}


@router.get("/api/contest/{contest_id}/problems", tags=["Contest"])
def contest_problems(contest_id: int, db: Session = Depends(get_db)):
    db_contest = db.query(Contest).filter(Contest.id == contest_id).first()
    if db_contest is None:
        raise HTTPException(status_code=404, detail="Contest Not Found")
    db_problems = (
        db.query(ContestProblem).filter(ContestProblem.contest_id == contest_id).all()
    )
    categories = []
    for db_problem in db_problems:
        db_category = (
            db.query(ContestProblemCategory)
            .filter(ContestProblemCategory.contest_problem_id == db_problem.id)
            .all()
        )
        category = []
        for cat in db_category:
            category.append(cat.category_id)
        categories.append(category)
    return {
        "id": db_contest.id,
        "title": db_contest.title,
        "slug": db_contest.slug,
        "description": db_contest.description,
        "time_limit": db_contest.time_limit,
        "memory_limit": db_contest.memory_limit,
        "input_format": db_contest.input_format,
        "sample_input": db_contest.sample_input,
        "output_format": db_contest.output_format,
        "sample_output": db_contest.sample_output,
        "constraints": db_contest.constraints,
        "explanation": db_contest.explanation,
        "created_at": db_contest.created_at,
        "updated_at": db_contest.updated_at,
        "categories": categories,
    }
    













@router.get("/api/contest/{contest_id}/scoreboard", tags=["Contest", "Scoreboard"])
def contest_scoreboard(contest_id: int, db: Session = Depends(get_db)):
    db_contest = db.query(Contest).filter(Contest.id == contest_id).first()
    if db_contest is None:
        raise HTTPException(status_code=404, detail="Contest Not Found")
    db_contestants = db.query(ContestParticipant).filter(ContestParticipant.contest_id == contest_id).all()
    db_problems = db.query(ContestProblem).filter(ContestProblem.contest_id == contest_id).all()
    problems_length = len(db_problems)
    contestants_length = len(db_contestants)
    logger.debug({"contest_id": contest_id, "contestants": db_contestants, "problems": db_problems})
    scoreboard = []
    for contestant in db_contestants:
        contestants_data = db.query(User).filter(User.id == contestant.user_id).first()
        problems = []
        total_time_used = 0
        score = 0
        user_attempted = 0
        for problem in db_problems:
            problem_data = db.query(ContestProblem).filter(ContestProblem.id == problem.id).first()

            # logger.debug({"problem_id": problem_data.id, "contest_id": contest_id, "user_id": contestant.user_id})

            submissions = db.query(ContestSubmission).filter(ContestSubmission.contest_id == contest_id, ContestSubmission.user_id == contestant.user_id, ContestSubmission.problem_id == problem.id).all()

            # logger.debug({"submission" : submissions})
            
            user_attempted += len(submissions)
            if len(submissions) == 0:
                problems.append({
                    "problem_id": problem_data.id, 
                    "attempted": 0,
                    "created_at": "Not Attempted",
                    "status": "Not Attempted"
                })
            elif len(submissions) > 1:
                status = submissions[0].status
                for submission in submissions:
                    total_time_used = total_time_used + ((submission.created_at - db_contest.start_time).total_seconds()/60)
                    # Cek jika ada submission AC, maka AC
                    if submission.status == "AC":
                        status = "AC"
                        score += 1
                        break
                problems.append({
                    "problem_id": problem_data.id, 
                    "attempted": len(submissions),
                    "created_at": submissions[0].created_at,
                    "status": status
                })
            else:
                total_time_used = total_time_used + ((submissions[0].created_at - db_contest.start_time).total_seconds()/60)
                if submissions[0].status == "AC":
                    score += 1
                problems.append({
                    "problem_id": problem_data.id, 
                    "attempted": len(submissions),
                    "created_at": submissions[0].created_at,
                    "status": submissions[0].status
                })
                
        scoreboard.append({
            "user": {
                "id" : contestants_data.id,
                "username": contestants_data.name,
                "score" : score,
                "attempted": user_attempted,
                "total_time_used": total_time_used
                },
            "problems": problems
        })
    sorted_data = sorted(scoreboard, key=lambda x: (x['user']['score'], -x['user']['total_time_used']), reverse=True)
    
    return {
        "contest": db_contest,
        "problem_length" : problems_length,
        "contestants_length" : contestants_length,
        "contestants": sorted_data
    }
    

@router.get("/api/contest/{contest_id}/user/{user_id}/problems/{problems_id}", tags=["Contest", "Testing"])
def contest_user_problems(contest_id: int, user_id: int, problems_id: int, db: Session = Depends(get_db)):
    db_contest = db.query(Contest).filter(Contest.id == contest_id).first()
    if db_contest is None:
        raise HTTPException(status_code=404, detail="Contest Not Found")
    db_contestants = db.query(ContestParticipant).filter(ContestParticipant.contest_id == contest_id, ContestParticipant.user_id == user_id).first()
    if db_contestants is None:
        raise HTTPException(status_code=404, detail="User Not Found")
    db_problems = db.query(ContestProblem).filter(ContestProblem.contest_id == contest_id, ContestProblem.id == problems_id).first()
    if db_problems is None:
        raise HTTPException(status_code=404, detail="Problem Not Found")
    db_submissions = db.query(ContestSubmission).filter(ContestSubmission.contest_id == contest_id, ContestSubmission.user_id == user_id, ContestSubmission.problem_id == problems_id).all()
    submissions = []
    for submission in db_submissions:
        submissions.append({
            "id": submission.id,
            "status": submission.status,
            "created_at": submission.created_at
        })
    return {
        "contest": db_contest,
        "user": db_contestants,
        "problem": db_problems,
        "submissions": submissions
    }