from fastapi import APIRouter, HTTPException
from database import SessionLocal
from models import TestCase, Problem
from pydantic import BaseModel

router = APIRouter()

class WriteTestCaseBase(BaseModel):
    problem_id : int
    input : str
    output : str

@router.get('/api/test_cases', tags=["Test Cases"])
def read_all_test_cases():
    db = SessionLocal()
    db_test_cases = db.query(TestCase).all()
    return db_test_cases    


@router.get('/api/test_case/{test_case_id}', tags=["Test Cases"])
def read_test_case(test_case_id : int):
    db = SessionLocal()
    db_test_case =   db.query(TestCase).filter(TestCase.id == test_case_id).first()
    return db_test_case

@router.get('/api/test_case/problem/{problem_id}', tags=["Test Cases", "Problems"])
def read_test_case_problem(problem_id : int):
    db = SessionLocal()
    db_test_case = db.query(TestCase).filter(TestCase.problem_id == problem_id).all()
    return db_test_case

@router.post("/api/test_case", tags=["Test Cases"])
def write_test_case(new_test_case : WriteTestCaseBase):
    db = SessionLocal()
    db_new_test_case = TestCase(problem_id = new_test_case.problem_id, input = new_test_case.input, output = new_test_case.output)
    db.add(db_new_test_case)
    db.commit()
    db.refresh(db_new_test_case)
    return {"message" : "Test case created successfully"}

@router.delete("/api/test_case/{test_case_id}", tags=["Test Cases"])
def delete_test_case(test_case_id : int):
    db = SessionLocal()
    db_test_case = db.query(TestCase).filter(TestCase.id == test_case_id).first()
    if db_test_case is None :
        raise HTTPException(statuc_code=404, detail="test_case not found")
    db.delete(db_test_case)
    db.commit()
    
    return {"message" : "Test case deleted succcesfully"}



    