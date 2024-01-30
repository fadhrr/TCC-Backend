from fastapi import APIRouter, HTTPException
from models import Submission
from pydantic import BaseModel
from database import SessionLocal


router = APIRouter()

class WriteSubmissionBase(BaseModel):
    user_id : str
    problem_id : int
    language_id : int
    status : str
    time : int
    memory : int

@router.get('/api/submissions', tags=["submissions"])
def read_all_submissions ():
    db = SessionLocal()    
    db_submissions_data = db.query(Submission).all()
    return db_submissions_data


@router.get('/api/submission/{submission_id}', tags=["submissions"])
def read_submission(submission_id:str):
    db = SessionLocal()
    db_submission_data = db.query(Submission).filter(Submission.id == submission_id).first()
    return db_submission_data


@router.post('/api/submission', tags=["submissions"])
def write_submission(new_submission : WriteSubmissionBase):
    db = SessionLocal()
    db_new_submission = Submission(
        user_id = new_submission.user_id,
        problem_id = new_submission.problem_id,
        language_id = new_submission.language_id,
        status = new_submission.status,
        time = new_submission.time,
        memory = new_submission.memory,
        )
    
    db.add(db_new_submission)
    db.commit()
    db.refresh(db_new_submission)
    return {"message" : "submission created successfully"}
    
    
@router.delete('/api/submission/{submission_id}', tags=["submissions"])
def delete_submission(submission_id : str):
    db = SessionLocal()
    submission_data = db.query(Submission).filter(Submission.id == submission_id).first()
    if submission_data is None:
        raise HTTPException(status_code=404, detail="submission data not found")
    db.delete(submission_data)
    db.commit()
    
    return {"message" : "submission deleted successfully"}
    
