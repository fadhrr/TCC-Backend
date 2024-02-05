from fastapi import APIRouter, HTTPException
from database import SessionLocal
from models import Contest 
from pydantic import BaseModel
from datetime import datetime
router = APIRouter()

class WriteContestBase(BaseModel):
    admin_id : str
    title : str
    slug : str
    description : str | None = None
    start_time : datetime
    end_time : datetime

class UpdateContestBase(BaseModel):
    title : str | None = None
    slug : str | None = None
    description : str | None = None
    start_time : datetime | None = None
    end_time : datetime | None = None


@router.get('/api/contests', tags=["Contest"])
def read_all_contests():
    db = SessionLocal()
    db_contests = db.query(Contest).all()
    return db_contests

@router.get('/api/contest/{contest_id}', tags=["Contest"])
def read_contest(contest_id:int):
    db = SessionLocal()
    
    
    db_contest = db.query(Contest).filter(Contest.id == contest_id).first()
    if db_contest is None:
        raise HTTPException(status_code = 404, detail="Contest Not Found")
    return db_contest
    
@router.post('/api/contest', tags=["Contest"])
def write_contest(new_contest : WriteContestBase):
    db = SessionLocal()
    new_db_contest = Contest(
        admin_id = new_contest.admin_id,
        title = new_contest.title,
        slug = new_contest.slug,
        description = new_contest.description,
        start_time = new_contest.start_time,
        end_time = new_contest.end_time
    )
    db.add(new_db_contest)
    db.commit()
    db.refresh(new_db_contest)
    return {"message" : "Contest created successfully"}

@router.put('/api/contest/{contest_id}', tags=["Contest"])
def update_contest(contest_id : int, updated_contest : UpdateContestBase):
    db = SessionLocal()
    new_updated_contest = db.query(Contest).filter(Contest.id == contest_id).first()
    if new_updated_contest is None :
        raise HTTPException(status_code = 404, detail="Contest Not Found")
    
    if updated_contest.title is not None :
        new_updated_contest.title = updated_contest.title
    
    if updated_contest.slug is not None :
        new_updated_contest.slug = updated_contest.slug

    if updated_contest.description is not None :
        new_updated_contest.description = updated_contest.description
    
    if updated_contest.start_time is not None :
        new_updated_contest.start_time = updated_contest.start_time
    
    if updated_contest.end_time is not None :
        new_updated_contest.end_time = updated_contest.end_time
    
    db.add(new_updated_contest)
    db.commit()
    db.refresh(new_updated_contest)
    
    return {"message" : "Contest updated succesfully"}

@router. delete('/api/contest/{contest_id}', tags=["Contest"])
def delete_contest(contest_id : int):
    db = SessionLocal()
    db_contest = db.query(Contest).filter(Contest.id == contest_id).first()
    db.delete(db_contest)
    db.commit()
    return {"message" : "Contest deleted succesfully"}