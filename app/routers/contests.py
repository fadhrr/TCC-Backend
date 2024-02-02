from fastapi import APIRouter, HTTPException
from database import SessionLocal
from models import Contest 

router = APIRouter()

@router.get('/api/contests', tags=["contests"])
def read_all_contests():
    db = SessionLocal()
    db_contests = db.query(Contest).all()
    return db

@router.get('/api/contest/{contest_id}', tags=["contests"])
def read_contest(contest_id:int):
    db = SessionLocal()
    db_contest = db.query(Contest).filter(Contest.id == contest_id).first()
    if db_contest is None:
        raise HTTPException(status_code = 404, detail="Contest Not Found")