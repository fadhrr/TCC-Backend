from fastapi import APIRouter, HTTPException
from models import Submission, User, TestCase, TestCaseResult, Language
from pydantic import BaseModel
from database import SessionLocal
from sqlalchemy import desc
import logging
import json



from dotenv import load_dotenv
import os
import httpx

logger = logging.getLogger("uvicorn")

router = APIRouter()

class WriteSubmissionBase(BaseModel):
    user_id : str
    problem_id : int
    language_id : int
    time : int
    memory : int
    code : str

@router.get('/api/submissions', tags=["Submission"])
def read_all_submissions ():
    db = SessionLocal()    
    db_submissions_data = db.query(Submission).all()
    return db_submissions_data


@router.get('/api/submission/{submission_id}', tags=["Submission"])
def read_submission(submission_id:str):
    db = SessionLocal()
    db_submission_data = db.query(Submission).filter(Submission.id == submission_id).first()
    return db_submission_data




@router.post('/api/submission', tags=["Submission"])
def write_submission(new_submission : WriteSubmissionBase):
    db = SessionLocal()
    db_new_submission = Submission(
        user_id = new_submission.user_id,
        problem_id = new_submission.problem_id,
        language_id = new_submission.language_id,
        time = new_submission.time,
        memory = new_submission.memory,
        code = new_submission.code
        )
    
    db.add(db_new_submission)
    db.commit()
    db.refresh(db_new_submission)
    
    # pass to FJudge
    
    # mendapatkan semua test case soal
    db_test_cases = db.query(TestCase).filter(TestCase.problem_id == new_submission.problem_id).all()
    test_cases = []
    for test_case in db_test_cases:
        test_cases.append({
            "input" : test_case.input,
            "expected_output" : test_case.output
        })
    
    language = db.query(Language).filter(Language.id == new_submission.language_id).first()
    payloads = {
        "identifier" : str(db_new_submission.id),
        "source_code" : db_new_submission.code,
        "language" : language.name,
        "test_cases" : test_cases
    }
    # logger.info("payloads\n")
    # logger.info(payloads)
    url = f"http://{os.getenv('JUDGER_HOST')}:{os.getenv('JUDGER_PORT')}/api/judge"
    res = httpx.post(url, json=payloads)
    # logger.info(res.text)
    result = json.loads(res.text)
    return result
    # return payloads
    
    
    
    
    
    
    
    return {"message" : "submission created successfully"}
    
    
@router.delete('/api/submission/{submission_id}', tags=["Submission"])
def delete_submission(submission_id : str):
    db = SessionLocal()
    submission_data = db.query(Submission).filter(Submission.id == submission_id).first()
    if submission_data is None:
        raise HTTPException(status_code=404, detail="submission data not found")
    db.delete(submission_data)
    db.commit()
    
    return {"message" : "submission deleted successfully"}
    
@router.get('/api/submissions/problem/{problem_id}', tags=["Submission"])
def read_submission_problems(problem_id :int):
    db = SessionLocal()
    db_submission = db.query(Submission).filter(Submission.problem_id == problem_id).all()
    return db_submission

@router.get('/api/submissions/user/{user_id}', tags=["Submission"])
def read_submission_problems(user_id :str):
    db = SessionLocal()
    db_submission = db.query(Submission).filter(Submission.user_id == user_id).all()
    return db_submission

@router.get('/api/submissions/user/{user_id}/problem/{problem_id}', tags=["Submission"])
def read_submission_problems(user_id :str, problem_id : int):
    db = SessionLocal()
    db_submission = db.query(Submission).filter(Submission.user_id == user_id, Submission.problem_id == problem_id).all()
    return db_submission


@router.get('/api/users/{problem_id}/submissions/topbytime', tags=["Submission", "User"])
def get_top_users_by_time(problem_id:int):
    db = SessionLocal()
    db_submissions = db.query(Submission).filter(Submission.status == "Accepted", Submission.problem_id == problem_id).order_by(Submission.time).limit(5).all()
    
    if not db_submissions:
        raise HTTPException(status_code=404, detail="No submissions found")
    
    top_users = []
    for submission in db_submissions:
        user_id = submission.user_id
        user = db.query(User).filter(User.id == user_id).first()
        time = submission.time
        top_users.append({"name": user.name, "time": time})
    
    return top_users

@router.get('/api/users/problem/{problem_id}/submissions/topbymemory', tags=["Submission", "User"])
def get_top_users_by_memory(problem_id:int):
    db = SessionLocal()
    db_submissions = db.query(Submission).filter(Submission.status == "Accepted", Submission.problem_id == problem_id).order_by(Submission.memory).limit(5).all()
    
    if not db_submissions:
        raise HTTPException(status_code=404, detail="No submissions found")
    
    top_users = []
    for submission in db_submissions:
        user_id = submission.user_id
        user = db.query(User).filter(User.id == user_id).first()
        memory = submission.memory
        top_users.append({"name": user.name, "memory": memory})
    
    return top_users



