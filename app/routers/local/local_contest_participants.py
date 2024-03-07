from fastapi import APIRouter
from ...database import SessionLocal
from ...models import LocalContestParticipant
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
    

class WriteLocalContestParticipantBase(BaseModel):
    contest_id : int
    user_id : str

@router.get("/api/local_contest/participants", tags=["Local Contest", "Local Contest Participant"])
def read_all_participants(db: Session = Depends(get_db)):
    
    
    db_contest_participants = db.query(LocalContestParticipant).all()
    return db_contest_participants

@router.get("/api/local_contest/{contest_id}/participants", tags=["Local Contest", "Local Contest Participant"])
def read_participants_contest(contest_id:int,db: Session = Depends(get_db)):
    
    
    db_contest_participants = db.query(LocalContestParticipant).filter(LocalContestParticipant.contest_id == contest_id).all()
    return db_contest_participants

@router.post("/api/local_contest/participant", tags=["Local Contest", "Local Contest Participant"])
def write_participants(new_contest_participant,db: Session = Depends(get_db)):
    
    
    db_new_contest_participant = LocalContestParticipant(contest_id = new_contest_participant.contest_id, user_id = new_contest_participant.user_id)
    db.add(db_new_contest_participant)
    db.commit()
    db.refresh(db_new_contest_participant)
    return {"Message" : "Local Contest participant inserted succesfully"}