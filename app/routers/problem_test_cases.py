from fastapi import APIRouter, HTTPException
from ..database import SessionLocal
from ..models import TestCase, Problem
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import Depends
router = APIRouter()

class WriteTestCaseBase(BaseModel):
    problem_id : int
    input : str
    output : str
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    

@router.get('/api/test_cases', tags=["Test Cases"])
def read_all_test_cases(db: Session = Depends(get_db)):
    
    
    db_test_cases = db.query(TestCase).all()
    return db_test_cases    


@router.get('/api/test_case/{test_case_id}', tags=["Test Cases"])
def read_test_case(test_case_id : int, db: Session = Depends(get_db)):
    
    
    db_test_case =   db.query(TestCase).filter(TestCase.id == test_case_id).first()
    return db_test_case

@router.get('/api/test_case/problem/{problem_id}', tags=["Test Cases", "Problem"])
def read_test_case_problem(problem_id : int, db: Session = Depends(get_db)):
    
    
    db_test_case = db.query(TestCase).filter(TestCase.problem_id == problem_id).all()
    return db_test_case

@router.post("/api/test_case", tags=["Test Cases"])
def write_test_case(new_test_case : WriteTestCaseBase, db: Session = Depends(get_db)):
    
    
    db_new_test_case = TestCase(problem_id = new_test_case.problem_id, input = new_test_case.input, output = new_test_case.output)
    db.add(db_new_test_case)
    db.commit()
    db.refresh(db_new_test_case)
    return {"message" : "Test case created successfully", "id" : db_new_test_case.id}

@router.delete("/api/test_case/{test_case_id}", tags=["Test Cases"])
def delete_test_case(test_case_id : int, db: Session = Depends(get_db)):
    
    
    db_test_case = db.query(TestCase).filter(TestCase.id == test_case_id).first()
    if db_test_case is None :
        raise HTTPException(statuc_code=404, detail="test_case not found")
    db.delete(db_test_case)
    db.commit()
    
    return {"message" : "Test case deleted succcesfully"}

@router.put("/api/test_case/{test_case_id}", tags=["Test Cases"])
def update_test_case(test_case_id: int, new_test_case: WriteTestCaseBase, db: Session = Depends(get_db)):
    test_case = db.query(TestCase).filter(TestCase.id == test_case_id).first()
    if not test_case:
        raise HTTPException(status_code=404, detail="Test Case not found")
    test_case.problem_id = new_test_case.problem_id
    test_case.input = new_test_case.input
    test_case.output = new_test_case.output
    db.add(test_case)
    db.commit()
    return {"message": "Test Case updated successfully"}



    