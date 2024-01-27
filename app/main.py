from typing import Union

from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models
from typing import Annotated
from pydantic import BaseModel



app = FastAPI()

class UserBase(BaseModel):
    name: str
    nim: str
    password: str
    score: int
    email: str
    

def get_users(db: Session, skip: int=0, limit: int=10):
    return db.query(models.User).offset(skip).limit(limit).all()

    
@app.post("/users")
def create_users(user: UserBase):
    db = SessionLocal()
    db_user = models.User(name=user.name, nim=user.nim, password=user.password, score=user.score, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/")
def read_users(skip: int=0, limit: int=10):
    db = SessionLocal()
    users = get_users(db, skip=skip, limit=limit)
    return users