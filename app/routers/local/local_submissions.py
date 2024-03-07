from fastapi import APIRouter, HTTPException
from ...models import LocalSubmission, User, LocalTestCase, LocalTestCaseResult, Language
from pydantic import BaseModel
from ...database import SessionLocal
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
class WriteLocalSubmissionBase(BaseModel):
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

@router.get('/api/local_submissions', tags=["Local Submission"])
def read_all_submissions (db: Session = Depends(get_db)):
    
        
    db_submissions_data = db.query(LocalSubmission).order_by(desc(LocalSubmission.created_at)).all()
    value = formatting_result(db_submissions_data, db)
    
    db.close()
    return value


@router.get('/api/local_submission/{submission_id}', tags=["Local Submission"])
def read_submission(submission_id:str,db: Session = Depends(get_db)):
    
    
    db_submission_data = db.query(LocalSubmission).filter(LocalSubmission.id == submission_id).first()
    if db_submission_data is None:
        raise HTTPException(status_code=404, detail="submission data not found")
    db_submission_data.status = formatting_status(db_submission_data.status)
    db.close()
    return db_submission_data




@router.post('/api/local_submission', tags=["Local Submission"])
def write_submission(new_submission : WriteLocalSubmissionBase,db: Session = Depends(get_db)):
    
    
    db_new_submission = LocalSubmission(
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
    db_test_cases = db.query(LocalTestCase).filter(LocalTestCase.problem_id == new_submission.problem_id).all()
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
    url = f"http://{os.getenv('JUDGER_HOST')}:{os.getenv('JUDGER_PORT')}/api/local_judge"
    res = httpx.post(url, json=payloads)
    # logger.info(res.text)
    result = json.loads(res.text)
    
    # add test case results to database
    test_case_results = result["results"]
    for test_case_result in test_case_results:
        db_test_case_result = LocalTestCaseResult(submission_id = db_new_submission.id, status = test_case_result["status"], time = test_case_result["time"])
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
    
    
@router.delete('/api/local_submission/{submission_id}', tags=["Local Submission"])
def delete_submission(submission_id : str,db: Session = Depends(get_db)):
    
    
    submission_data = db.query(LocalSubmission).filter(LocalSubmission.id == submission_id).first()
    if submission_data is None:
        raise HTTPException(status_code=404, detail="submission data not found")
    db.delete(submission_data)
    db.commit()
    
    db.close()
    return {"message" : "submission deleted successfully"}
    
@router.get('/api/local_submissions/problem/{problem_id}', tags=["Local Submission"])
def read_submission_problems(problem_id :int,db: Session = Depends(get_db)):
    
    
    db_submission = db.query(LocalSubmission).filter(LocalSubmission.problem_id == problem_id).all()
    value = formatting_result(db_submission, db)
    db.close()
    return value

@router.get('/api/local_submissions/user/{user_id}', tags=["Local Submission"])
def read_submission_problems(user_id :str,db: Session = Depends(get_db)):
    
    
    db_submission = db.query(LocalSubmission).filter(LocalSubmission.user_id == user_id).all()
    value = formatting_result(db_submission, db)
    db.close()
    return value

@router.get('/api/local_submissions/user/{user_id}/problem/{problem_id}', tags=["Local Submission"])
def read_submission_problems(user_id :str, problem_id : int,db: Session = Depends(get_db)):
    
    
    db_submission = db.query(LocalSubmission).filter(LocalSubmission.user_id == user_id, LocalSubmission.problem_id == problem_id).all()
    value = formatting_result(db_submission, db)
    db.close()
    return value


@router.get('/api/users/{problem_id}/local_submissions/topbytime', tags=["Local Submission", "User"])
def get_top_users_by_time(problem_id:int,db: Session = Depends(get_db)):
    
    
    db_submissions = db.query(LocalSubmission).filter(LocalSubmission.status == "Accepted", LocalSubmission.problem_id == problem_id).order_by(LocalSubmission.time).limit(5).all()
    
    if not db_submissions:
        raise HTTPException(status_code=404, detail="No submissions found")
    
    top_users = []
    for submission in db_submissions:
        user_id = submission.user_id
        user = db.query(User).filter(User.id == user_id).first()
        time = submission.time
        top_users.append({"name": user.name, "time": time})
    
    db.close()
    return top_users

@router.get('/api/local_users/problem/{problem_id}/local_submissions/topbymemory', tags=["Local Submission", "User"])
def get_top_users_by_memory(problem_id:int,db: Session = Depends(get_db)):
    
    
    db_submissions = db.query(LocalSubmission).filter(LocalSubmission.status == "Accepted", LocalSubmission.problem_id == problem_id).order_by(LocalSubmission.memory).limit(5).all()
    
    if not db_submissions:
        raise HTTPException(status_code=404, detail="No submissions found")
    
    top_users = []
    for submission in db_submissions:
        user_id = submission.user_id
        user = db.query(User).filter(User.id == user_id).first()
        memory = submission.memory
        top_users.append({"name": user.name, "memory": memory})
    
    db.close()
    return top_users



