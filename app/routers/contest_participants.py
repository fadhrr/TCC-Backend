from fastapi import APIRouter, HTTPException
from ..database import SessionLocal
from ..models import ContestParticipant, Contest
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
def read_all_contests_participants(db: Session = Depends(get_db)):
    
    db_contest_participants = db.query(ContestParticipant).all()
    return db_contest_participants


@router.get("/api/contest/{contest_id}/participants", tags=["Contest", "Contest Participant"])
def read_participants_contest(contest_id:int,db: Session = Depends(get_db)):
    
    db_contest_participants = db.query(ContestParticipant).filter(ContestParticipant.contest_id == contest_id).all()
    return db_contest_participants


@router.get("/api/contest/{contest_id}/participant/{user_id}", tags=["Contest", "Contest Participant"])
def read_contest_participant_by_id(contest_id : int, user_id : str, db : Session = Depends(get_db)):
    db_participant = db.query(ContestParticipant).filter(ContestParticipant.contest_id == contest_id, ContestParticipant.user_id == user_id).first()
    if db_participant is None :
        raise HTTPException(status_code=400, detail="User not found in this contest")
    return db_participant


@router.post("/api/contest/participant", tags=["Contest", "Contest Participant"])
def write_participants(new_contest_participant : WriteContestParticipantBase,db: Session = Depends(get_db)):
        
    db_new_contest_participant = ContestParticipant(contest_id = new_contest_participant.contest_id, user_id = new_contest_participant.user_id)
    db.add(db_new_contest_participant)
    db.commit()
    db.refresh(db_new_contest_participant)
    return {"Message" : "Contest participant inserted succesfully", "id" : db_new_contest_participant.id}


@router.delete("/api/contest/{contest_id}/participant/{user_id}", tags=["Contest", "Contest Participant"])
def delete_participant(contest_id: int, user_id: str, db : Session = Depends(get_db)):
    
    db_participant = db.query(ContestParticipant).filter(ContestParticipant.contest_id == contest_id, ContestParticipant.user_id == user_id).first()
    if db_participant is None :
        raise HTTPException(status_code=404, detail="No participant found on this contest")
    db.delete(db_participant)
    db.commit()
    return {"message" : "participant has been deleted"}
    


