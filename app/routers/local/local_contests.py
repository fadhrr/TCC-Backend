from fastapi import APIRouter, HTTPException
from database import SessionLocal
from models import LocalContest 
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import Depends
 

router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    

class WriteLocalContestBase(BaseModel):
    admin_id : str
    title : str
    slug : str
    description : str | None = None
    start_time : datetime
    end_time : datetime

class UpdateLocalContestBase(BaseModel):
    title : str | None = None
    slug : str | None = None
    description : str | None = None
    start_time : datetime | None = None
    end_time : datetime | None = None


@router.get('/api/local_contests', tags=["Local Contest"])
def read_all_contests(db: Session = Depends(get_db)):
    
    
    db_contests = db.query(LocalContest).all()
    return db_contests

@router.get('/api/local_contest/{contest_id}', tags=["Local Contest"])
def read_contest(contest_id:int,db: Session = Depends(get_db)):
    
    db_contest = db.query(LocalContest).filter(LocalContest.id == contest_id).first()
    if db_contest is None:
        raise HTTPException(status_code = 404, detail="Local Contest Not Found")
    return db_contest
    
@router.post('/api/local_contest', tags=["Local Contest"])
def write_contest(new_contest : WriteLocalContestBase,db: Session = Depends(get_db)):
    
    
    new_db_contest = LocalContest(
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
    return {"message" : "Local Contest created successfully"}

@router.put('/api/local_contest/{contest_id}', tags=["Local Contest"])
def update_contest(contest_id : int, updated_contest : UpdateLocalContestBase,db: Session = Depends(get_db)):
    
    
    new_updated_contest = db.query(LocalContest).filter(LocalContest.id == contest_id).first()
    if new_updated_contest is None :
        raise HTTPException(status_code = 404, detail="Local Contest Not Found")
    
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
    
    return {"message" : "Local Contest updated succesfully"}

@router. delete('/api/local_contest/{contest_id}', tags=["Local Contest"])
def delete_contest(contest_id : int,db: Session = Depends(get_db)):
    
    
    db_contest = db.query(LocalContest).filter(LocalContest.id == contest_id).first()
    db.delete(db_contest)
    db.commit()
    return {"message" : "Local Contest deleted succesfully"}