from typing import Annotated, Optional
from fastapi import APIRouter, Depends, Path, Query, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy import desc
from pydantic import BaseModel
from database import SessionLocal
from models import User, Admin
from sqlalchemy.orm import Session


router = APIRouter()

class WriteUserBase(BaseModel):
    id : str
    name: str
    nim: str
    score: int | None = None
    email: str
    
class UpdateUserBase(BaseModel):
    name: str | None = None
    nim: str | None = None
    score: int | None = None 
    email: str | None = None
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    


@router.get("/api/users", tags=["User"])
def read_all_users():
    db = SessionLocal()
    users = db.query(User).all()
    return users

@router.get("/api/users/role", tags=["User"])
def read_all_users_with_role():
    db = SessionLocal()
    users = db.query(User).all()

    #
    values = []
    for user in users:
        data_admin = db.query(Admin).filter(Admin.user_id == user.id).first()
        role = ""
        if data_admin :
            if data_admin.role == 1 :
                role = "Assistant"
            elif data_admin.role == 2 :
                role = "Admin"
        values.append({
            "id" : user.id,
            "name" : user.name,
            "nim" : user.nim,
            "score" : user.score,
            "email" : user.email,
            "role" : role,
            "created_at" : user.created_at
        })
    return values

@router.get("/api/user/{user_id}", tags=["User"])
def read_user(user_id : Annotated[str, Path(title="Id user yang ingin diambil")]):
    db = SessionLocal();
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/api/user", tags=["User"])
def write_user(user: WriteUserBase):
    db = SessionLocal()
    user = User(id = user.id, name=user.name, nim=user.nim, score=0, email=user.email)
    db.add(user)
    db.commit()
    user_dict = jsonable_encoder(user)
    return JSONResponse(content={
        "status" : "User created succesfully",
        "user" : user_dict
    })

@router.put("/api/user/{user_id}", tags=["User"])
async def update_user(user_id: str, user_data: UpdateUserBase, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
  
    if user_data.name is not None :
        user.name = user_data.name
    
    if user_data.nim is not None :
        user.nim = user_data.nim
    
    if user_data.score is not None :
        user.score = user_data.score
    
    if user_data.email is not None :
        user.email = user_data.email
    
        
    db.add(user)
    db.commit()

    return {"message": "User updated successfully"}

@router.delete("/api/user/{user_id}", tags=["User"])
def delete_user(user_id: Annotated[str, Path(title="Id user yang ingin di delete")]):
    db = SessionLocal()
    user = db.query(User).filter(User.id==user_id).first()
    if user is None :
        raise HTTPException(status_code=404, detail="User was not found")
    db.delete(user)
    db.commit()
    
    return {"message" : "User deleted successfully"}
   
@router.get("/api/leaderboard", tags=["User"])
def get_leaderboard():
    db = SessionLocal()
    user = db.query(User).order_by(desc(User.score)).all()
    return user
