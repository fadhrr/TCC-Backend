from fastapi import APIRouter
from database import SessionLocal
from models import ContestParticipant
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import Depends
 

router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    

class WriteContestParticipantBase(BaseModel):
    contest_id : int
    user_id : str

@router.get("/api/contest/participants", tags=["Contest", "Contest Participant"])
def read_all_participants(db: Session = Depends(get_db)):
    
    
    db_contest_participants = db.query(ContestParticipant).all()
    return db_contest_participants

@router.get("/api/contest/{contest_id}/participants", tags=["Contest", "Contest Participant"])
def read_participants_contest(contest_id:int,db: Session = Depends(get_db)):
    
    
    db_contest_participants = db.query(ContestParticipant).filter(ContestParticipant.contest_id == contest_id).all()
    return db_contest_participants

@router.post("/api/contest/participant", tags=["Contest", "Contest Participant"])
def write_participants(new_contest_participant,db: Session = Depends(get_db)):
    
    
    db_new_contest_participant = ContestParticipant(contest_id = new_contest_participant.contest_id, user_id = new_contest_participant.user_id)
    db.add(db_new_contest_participant)
    db.commit()
    db.refresh(db_new_contest_participant)
    return {"Message" : "Contest participant inserted succesfully"}