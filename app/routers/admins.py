from fastapi import APIRouter, HTTPException
from models import Admin
from pydantic import BaseModel
from database import SessionLocal


router = APIRouter()

class WriteAdminBase(BaseModel):
    id : str
    user_id : str
    role : int | None = None

@router.get('/api/admins', tags=["admins"])
def read_all_admins ():
    db = SessionLocal()    
    db_admins_data = db.query(Admin).all()
    return db_admins_data

@router.get('/api/admin/{admin_id}', tags=["admins"])
def read_admin(admin_id:str):
    db = SessionLocal()
    db_admin_data = db.query(Admin).filter(Admin.id == admin_id).first()
    return db_admin_data

@router.post('/api/admin', tags=["admins"])
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
    
@router.delete('/api/admin/{admin_id}', tags=["admins"])
def delete_admin(admin_id : str):
    db = SessionLocal()
    admin_data = db.query(Admin).filter(Admin.id == admin_id).first()
    if admin_data is None:
        raise HTTPException(status_code=404, detail="Admin data not found")
    db.delete(admin_data)
    db.commit()
    
    return {"message" : "Admin deleted successfully"}
    
