from typing import Union

from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models
from typing import Annotated
from pydantic import BaseModel
from routers import users



app = FastAPI()

class UserBase(BaseModel):
    name: str
    nim: str
    password: str
    score: int
    email: str
    

app.include_router(users.router)


