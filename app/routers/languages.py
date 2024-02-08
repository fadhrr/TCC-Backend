from fastapi import APIRouter
from pydantic import BaseModel
from models import Language
from database import SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends
 
class WriteLanguageBase(BaseModel):
    name : str
    
    
router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    

@router.post('/api/language', tags={"Language"})
def write_language(new_lg : WriteLanguageBase,db: Session = Depends(get_db)):
    
    
    db_lg = Language(name = new_lg.name)
    db.add(db_lg)
    db.commit()
    db.refresh(db_lg)
    return {"message" : "Language created successfully"}
