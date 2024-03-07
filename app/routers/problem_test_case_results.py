from fastapi import APIRouter, HTTPException
from ..database import SessionLocal
from ..models import TestCaseResult
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import Depends
 
router = APIRouter()

class WriteTestCaseResultBase(BaseModel):
    submission_id : int
    status : str
    time : int
    memory : int
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
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
def formatting_result(db_datas):
    for db_data in db_datas:
        db_data.status = formatting_status(db_data.status)
    return db_datas

# format satu result untuk bisa dibaca oleh user
# def formatting_result(db_datas):
#     for db_data in db_datas:
#         db_data.status = formatting_status(db_data.status)
#     return db_datas

    

@router.get('/api/test_case_results', tags=["Test Case Results"])
def read_all_test_case_results(db: Session = Depends(get_db)):
    
    
    db_test_case_results = db.query(TestCaseResult).all()
    db_test_case_results = formatting_result(db_test_case_results)
    return db_test_case_results

@router.get('/api/test_case_result/{test_case_result_id}', tags=["Test Case Results"])
def read_test_case_result(test_case_result_id : int,db: Session = Depends(get_db)):
    
    
    db_test_case_result = db.query(TestCaseResult).filter(TestCaseResult.id == test_case_result_id).first()
    db_test_case_result = formatting_status(db_test_case_result.status)
    return db_test_case_result

@router.get("/api/get/test_case_result/{submission_id}", tags=["Test Case Results"])
def get_test_case_result(submission_id : int,db: Session = Depends(get_db)):
    
    
    db_test_case_result = db.query(TestCaseResult).filter(TestCaseResult.submission_id == submission_id).all()
    db_test_case_result = formatting_result(db_test_case_result)
    return db_test_case_result

@router.get('/api/test_case_result/submission/{submission_id}', tags=["Test Case Results", "Submission"])
def read_test_case_result_submission(submission_id : str,db: Session = Depends(get_db)):
    
    
    db_test_case_result = db.query(TestCaseResult).filter(TestCaseResult.submission_id == submission_id).all()
    db_test_case_result = formatting_result(db_test_case_result)
    return db_test_case_result

@router.post("/api/test_case_result", tags=["Test Case Results"])
def write_test_case_result(new_test_case_result : WriteTestCaseResultBase,db: Session = Depends(get_db)):
    
    
    db_new_test_case_result = TestCaseResult(
        submission_id = new_test_case_result.submission_id,
        status = new_test_case_result.status,
        time = new_test_case_result.time,
        memory = new_test_case_result.memory
    )
    db.add(db_new_test_case_result)
    db.commit()
    db.refresh(db_new_test_case_result)
    return {"message" : "Test case result created successfully"}

@router.delete("/api/test_case_result/{test_case_result_id}", tags=["Test Case Results"])
def delete_test_case_result(test_case_result_id : int,db: Session = Depends(get_db)):
    
    
    db_test_case_result = db.query(TestCaseResult).filter(TestCaseResult.id == test_case_result_id).first()
    if db_test_case_result is None :
        raise HTTPException(statuc_code=404, detail="Test case result not found")
    db.delete(db_test_case_result)
    db.commit()
    
    return {"message" : "Test case result deleted succcesfully"}
