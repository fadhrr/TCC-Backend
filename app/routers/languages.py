from fastapi import APIRouter
from pydantic import BaseModel
from models import Language
from database import SessionLocal

class WriteLanguageBase(BaseModel):
    name : str
    
    
router = APIRouter()

@router.post('/api/language', tags={"languages"})
def write_language(new_lg : WriteLanguageBase):
    db = SessionLocal()
    db_lg = Language(name = new_lg.name)
    db.add(db_lg)
    db.commit()
    db.refresh(db_lg)
    return {"message" : "Language created successfully"}
