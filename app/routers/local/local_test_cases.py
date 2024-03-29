from fastapi import APIRouter, HTTPException
from ...database import SessionLocal
from ...models import LocalTestCase, Problem
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import Depends
router = APIRouter()

class WriteLocalTestCaseBase(BaseModel):
    problem_id : int
    input : str
    output : str
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    

@router.get('/api/local_test_cases', tags=["Test Cases"])
def read_all_test_cases(db: Session = Depends(get_db)):
    
    
    db_test_cases = db.query(LocalTestCase).all()
    return db_test_cases    


@router.get('/api/local_test_case/{local_test_case_id}', tags=["Test Cases"])
def read_test_case(test_case_id : int, db: Session = Depends(get_db)):
    
    
    db_test_case =   db.query(LocalTestCase).filter(LocalTestCase.id == test_case_id).first()
    return db_test_case

@router.get('/api/local_test_case/problem/{problem_id}', tags=["Test Cases", "Problem"])
def read_test_case_problem(problem_id : int, db: Session = Depends(get_db)):
    
    
    db_test_case = db.query(LocalTestCase).filter(LocalTestCase.problem_id == problem_id).all()
    return db_test_case

@router.post("/api/local_test_case", tags=["Test Cases"])
def write_test_case(new_test_case : WriteLocalTestCaseBase, db: Session = Depends(get_db)):
    
    
    db_new_test_case = LocalTestCase(problem_id = new_test_case.problem_id, input = new_test_case.input, output = new_test_case.output)
    db.add(db_new_test_case)
    db.commit()
    db.refresh(db_new_test_case)
    return {"message" : "Test case created successfully"}

@router.delete("/api/local_test_case/{local_test_case_id}", tags=["Test Cases"])
def delete_test_case(test_case_id : int, db: Session = Depends(get_db)):
    
    
    db_test_case = db.query(LocalTestCase).filter(LocalTestCase.id == test_case_id).first()
    if db_test_case is None :
        raise HTTPException(statuc_code=404, detail="test_case not found")
    db.delete(db_test_case)
    db.commit()
    
    return {"message" : "Test case deleted succcesfully"}



    