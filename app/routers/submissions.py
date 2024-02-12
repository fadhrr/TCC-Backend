from fastapi import APIRouter, HTTPException
from models import Submission, User, TestCase, TestCaseResult, Language
from pydantic import BaseModel
from database import SessionLocal
from sqlalchemy import desc
import logging
import json
from sqlalchemy.orm import Session
from fastapi import Depends
 

from dotenv import load_dotenv
import os
import httpx

logger = logging.getLogger("uvicorn")
router = APIRouter()
class WriteSubmissionBase(BaseModel):
    user_id : str
    problem_id : int
    language_id : int
    time : float
    memory : int
    code : str
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    

# format status untuk bisa dibaca oleh user
def formatting_status(result):
    if result == "AC":
        return "Accepted"
    elif result == "WA" :
        return "Wrong Answer"
    elif result == "RTE" :
        return "Runtime Error"
    elif result == "TLE" :
        return "Time Limit Exceeded"
    elif result == "CTE":
        return "Compile Time Error"
    else:
        return result
    
# format result untuk bisa dibaca oleh user
def formatting_result(db_submissions_data, db):
    for db_submission in db_submissions_data:
        db_submission.status = formatting_status(db_submission.status)
    return db_submissions_data

@router.get('/api/submissions', tags=["Submission"])
def read_all_submissions (db: Session = Depends(get_db)):
    
        
    db_submissions_data = db.query(Submission).order_by(desc(Submission.created_at)).all()
    value = formatting_result(db_submissions_data, db)
    
    db.close()
    return value


@router.get('/api/submission/{submission_id}', tags=["Submission"])
def read_submission(submission_id:str,db: Session = Depends(get_db)):
    
    
    db_submission_data = db.query(Submission).filter(Submission.id == submission_id).first()
    if db_submission_data is None:
        raise HTTPException(status_code=404, detail="submission data not found")
    db_submission_data.status = formatting_status(db_submission_data.status)
    db.close()
    return db_submission_data




@router.post('/api/submission', tags=["Submission"])
def write_submission(new_submission : WriteSubmissionBase,db: Session = Depends(get_db)):
    
    
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
    

    payloads = {
        "identifier" : db_new_submission.id,
        "source_code" : db_new_submission.code,
        "language_id" : db_new_submission.language_id,
        "test_cases" : test_cases
    }
    # logger.info("payloads\n")
    # logger.info(payloads)
    url = f"http://{os.getenv('JUDGER_HOST')}:{os.getenv('JUDGER_PORT')}/api/judge"
    res = httpx.post(url, json=payloads)
    # logger.info(res.text)
    result = json.loads(res.text)
    
    # add test case results to database
    test_case_results = result["results"]
    for test_case_result in test_case_results:
        db_test_case_result = TestCaseResult(submission_id = db_new_submission.id, status = test_case_result["status"], time = test_case_result["time"])
        db.add(db_test_case_result)
    
    # add submission result to database
    
    db_new_submission.status = result["verdict"]
    db_new_submission.time = result["avg_time"]
    # db_new_submission.memory = result["avg_memory"]   
    db.add(db_new_submission)
    db.commit()
    db.refresh(db_new_submission)
   
    
    db.close()
    # return result
 
    return {"message" : "submission created successfully"}
    
    
@router.delete('/api/submission/{submission_id}', tags=["Submission"])
def delete_submission(submission_id : str,db: Session = Depends(get_db)):
    
    
    submission_data = db.query(Submission).filter(Submission.id == submission_id).first()
    if submission_data is None:
        raise HTTPException(status_code=404, detail="submission data not found")
    db.delete(submission_data)
    db.commit()
    
    db.close()
    return {"message" : "submission deleted successfully"}
    
@router.get('/api/submissions/problem/{problem_id}', tags=["Submission"])
def read_submission_problems(problem_id :int,db: Session = Depends(get_db)):
    
    
    db_submission = db.query(Submission).filter(Submission.problem_id == problem_id).all()
    value = formatting_result(db_submission, db)
    db.close()
    return value

@router.get('/api/submissions/user/{user_id}', tags=["Submission"])
def read_submission_problems(user_id :str,db: Session = Depends(get_db)):
    
    
    db_submission = db.query(Submission).filter(Submission.user_id == user_id).all()
    value = formatting_result(db_submission, db)
    db.close()
    return value

@router.get('/api/submissions/user/{user_id}/problem/{problem_id}', tags=["Submission"])
def read_submission_problems(user_id :str, problem_id : int,db: Session = Depends(get_db)):
    
    
    db_submission = db.query(Submission).filter(Submission.user_id == user_id, Submission.problem_id == problem_id).all()
    value = formatting_result(db_submission, db)
    db.close()
    return value


@router.get('/api/users/{problem_id}/submissions/topbytime', tags=["Submission", "User"])
def get_top_users_by_time(problem_id:int,db: Session = Depends(get_db)):
    
    
    db_submissions = db.query(Submission).filter(Submission.status == "AC", Submission.problem_id == problem_id).order_by(Submission.time).limit(5).all()
    
    if db_submissions is None:
        raise HTTPException(status_code=404, detail="No submissions found")
    
    top_users = []
    for submission in db_submissions:
        user_id = submission.user_id
        user = db.query(User).filter(User.id == user_id).first()
        time = submission.time
        top_users.append({"name": user.name, "time": time})
    
    db.close()
    return top_users

@router.get('/api/users/problem/{problem_id}/submissions/topbymemory', tags=["Submission", "User"])
def get_top_users_by_memory(problem_id:int,db: Session = Depends(get_db)):
    
    
    db_submissions = db.query(Submission).filter(Submission.status == "AC", Submission.problem_id == problem_id).order_by(Submission.memory).limit(5).all()
    
    if db_submissions is None:
        raise HTTPException(status_code=404, detail="No submissions found")
    
    top_users = []
    for submission in db_submissions:
        user_id = submission.user_id
        user = db.query(User).filter(User.id == user_id).first()
        memory = submission.memory
        top_users.append({"name": user.name, "memory": memory})
    
    db.close()
    return top_users



