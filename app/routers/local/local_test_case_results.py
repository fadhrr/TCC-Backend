from fastapi import APIRouter, HTTPException
from database import SessionLocal
from models import LocalTestCaseResult
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import Depends
 
router = APIRouter()

class WriteLocalTestCaseResultBase(BaseModel):
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
    

@router.get('/api/local_test_case_results', tags=["Local Test Case Results"])
def read_all_test_case_results(db: Session = Depends(get_db)):
    
    
    db_test_case_results = db.query(LocalTestCaseResult).all()
    return db_test_case_results

@router.get('/api/local_test_case_result/{test_case_result_id}', tags=["Local Test Case Results"])
def read_test_case_result(test_case_result_id : int,db: Session = Depends(get_db)):
    
    
    db_test_case_result = db.query(LocalTestCaseResult).filter(LocalTestCaseResult.id == test_case_result_id).first()
    return db_test_case_result

@router.get("/api/get/local_test_case_result/{submission_id}", tags=["Local Test Case Results"])
def get_test_case_result(submission_id : int,db: Session = Depends(get_db)):
    
    
    db_test_case_result = db.query(LocalTestCaseResult).filter(LocalTestCaseResult.submission_id == submission_id).all()
    return db_test_case_result

@router.get('/api/local_test_case_result/submission/{submission_id}', tags=["Local Test Case Results", "Submission"])
def read_test_case_result_submission(submission_id : str,db: Session = Depends(get_db)):
    
    
    db_test_case_result = db.query(LocalTestCaseResult).filter(LocalTestCaseResult.submission_id == submission_id).all()
    return db_test_case_result

@router.post("/api/local_test_case_result", tags=["Local Test Case Results"])
def write_test_case_result(new_test_case_result : WriteLocalTestCaseResultBase,db: Session = Depends(get_db)):
    
    
    db_new_test_case_result = LocalTestCaseResult(
        submission_id = new_test_case_result.submission_id,
        status = new_test_case_result.status,
        time = new_test_case_result.time,
        memory = new_test_case_result.memory
    )
    db.add(db_new_test_case_result)
    db.commit()
    db.refresh(db_new_test_case_result)
    return {"message" : "Local test case result created successfully"}

@router.delete("/api/local_test_case_result/{test_case_result_id}", tags=["Local Test Case Results"])
def delete_test_case_result(test_case_result_id : int,db: Session = Depends(get_db)):
    
    
    db_test_case_result = db.query(LocalTestCaseResult).filter(LocalTestCaseResult.id == test_case_result_id).first()
    if db_test_case_result is None :
        raise HTTPException(statuc_code=404, detail="Local test case result not found")
    db.delete(db_test_case_result)
    db.commit()
    
    return {"message" : "Local test case result deleted succcesfully"}
