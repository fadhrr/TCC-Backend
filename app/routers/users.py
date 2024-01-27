from typing import Annotated, Optional
from fastapi import APIRouter, Path, Query, HTTPException
from pydantic import BaseModel
from database import SessionLocal
from models import User

router = APIRouter()

class UserBase(BaseModel):
    id : str
    name: str
    nim: str
    password: str
    score: int | None = None
    email: str
    
class UpdateUserBase(BaseModel):
    name: Optional[str] 
    nim: Optional[str] 
    password: Optional[str] 
    score: Optional[int] 
    email: Optional[str] 
    

@router.get("/api/users")
def read_all_users():
    db = SessionLocal()
    users = db.query(User).all()
    return users

@router.get("/api/user/{user_id}")
def read_user(user_id : Annotated[int, Path(title="Id user yang ingin diambil")]):
    db = SessionLocal();
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/api/user")
def write_user(user: UserBase):
    db = SessionLocal()
    user = User(id = user.id, name=user.name, nim=user.nim, password=user.password, score=0, email=user.email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return(user)

@router.put("api/user/{user_id}")
def update_user(user_id : Annotated[int, Path(title="Id user yang ingin di ganti")], userUpdated: UpdateUserBase):
    db = SessionLocal()
    db_user = db_user = db.query(User).filter(User.id == user_id).one_or_none()


    if db_user is None :
        raise HTTPException(status_code=404, detail="User not found")
    if userUpdated.name != None :
        db_user.name = userUpdated.name
        
    if userUpdated.nim != None :
        db_user.nim = userUpdated.nim
        
    if userUpdated.password != None :
        db_user.password = userUpdated.password
        
    if userUpdated.score != None :
        db_user.score = userUpdated.score
        
    if userUpdated.email != None :
        db_user.email = userUpdated.email
  
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.delete("/api/user/{user_id}")
def delete_user(user_id: Annotated[int, Path(title="Id user yang ingin di delete")]):
    db = SessionLocal()
    user = db.query(User).filter(User.id==user_id).first()
    if user is None :
        raise HTTPException(status_code=404, detail="User was not found")
    db.delete(user)
    db.commit()
   