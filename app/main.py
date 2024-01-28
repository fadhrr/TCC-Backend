from typing import Union

from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models
from typing import Annotated
from pydantic import BaseModel
from routers import users, problems



app = FastAPI(
    title="TCC API",
    description="**TCC (Training Code Center)** adalah wadah belajar pemrograman kompetitif yang dirancang khusus untuk mahasiswa Universitas Syiah Kuala (USK). Platform ini memungkinkan pengguna untuk mengasah keterampilan dalam menyelesaikan berbagai tantangan pemrograman. Setiap jawaban yang benar akan memberikan pengguna poin, dan ada sejumlah tingkatan prestasi, seperti \"Sepuh\", \"Master\", dan \"Pemula\", yang mencerminkan tingkat keahlian berdasarkan jumlah poin yang diperoleh. \nBerikut adalah TCC Data API",
    version="0.0.1",
    contact={
        "name": "Admin",
        "email": "tccadmin@gmail.com",
    },
    license_info={
        "name": "MIT",
    }
)

class UserBase(BaseModel):
    name: str
    nim: str
    password: str
    score: int
    email: str
    

app.include_router(users.router)
app.include_router(problems.router)


