from typing import Union

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from .routers import problem_test_case_results, problem_test_cases
from .routers import users, problems, admins, languages, submissions, categories, contests, contest_participants, contest_problems, notification
from .database import engine, SessionLocal
from typing import Annotated
from pydantic import BaseModel

from .routers.local import local_test_cases, local_test_case_results , local_contests, local_contest_participants, local_contest_problems
from fastapi.middleware.cors import CORSMiddleware


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

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET", "PUT", "DELETE"],
    allow_headers=["*"],
)


# otomatis pindah ke /docs ketika landing 

@app.get('/', tags=["Landing Path"])
def redirect():
    return RedirectResponse('/docs')

# router 
app.include_router(users.router)
app.include_router(problems.router)
app.include_router(admins.router)
app.include_router(submissions.router)
app.include_router(languages.router)
app.include_router(categories.router)
app.include_router(contests.router)
app.include_router(contest_participants.router)
app.include_router(contest_problems.router)
app.include_router(problem_test_cases.router)
app.include_router(problem_test_case_results.router)
app.include_router(notification.router)

# app.include_router(local_test_cases.router)
# app.include_router(local_test_case_results.router)
# app.include_router(local_contests.router)
# app.include_router(local_contest_participants.router)
# app.include_router(local_contest_problems.router)



