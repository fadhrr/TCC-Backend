from fastapi import APIRouter, HTTPException
from models import Admin
from pydantic import BaseModel
from database import SessionLocal


router = APIRouter()

class WriteAdminBase(BaseModel):
    id : str
    user_id : str
    role : int | None = None

@router.get('/api/admins', tags=["Admin"])
def read_all_admins ():
    db = SessionLocal()    
    db_admins_data = db.query(Admin).all()
    return db_admins_data

@router.get('/api/admin/{admin_id}', tags=["Admin"])
def read_admin(admin_id:str):
    db = SessionLocal()
    db_admin_data = db.query(Admin).filter(Admin.id == admin_id).first()
    return db_admin_data

@router.post('/api/admin', tags=["Admin"])
def write_admin(new_admin : WriteAdminBase):
    db = SessionLocal()
    db_new_admin = Admin(id = new_admin.id, user_id = new_admin.user_id)
    
    if new_admin.role is None :
        db_new_admin.role = 1
    else :
        db_new_admin.role = new_admin.role
    
    db.add(db_new_admin)
    db.commit()
    db.refresh(db_new_admin)
    return {"message" : "Admin created successfully"}
    
@router.delete('/api/admin/{admin_id}', tags=["Admin"])
def delete_admin(admin_id : str):
    db = SessionLocal()
    admin_data = db.query(Admin).filter(Admin.id == admin_id).first()
    if admin_data is None:
        raise HTTPException(status_code=404, detail="Admin data not found")
    db.delete(admin_data)
    db.commit()
    
    return {"message" : "Admin deleted successfully"}
    
@router.get("/api/role/assistants", tags=["User", "Admin", "Assistant"])
def get_assistant():
    db = SessionLocal()
    user = db.query(Admin).filter(Admin.role == 1).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Assistant not found")
    return user

@router.get("/api/role/admins", tags=["User", "Admin", "Assistant"])
def get_assistant():
    db = SessionLocal()
    user = db.query(Admin).filter(Admin.role == 2).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Assistant not found")
    return user
