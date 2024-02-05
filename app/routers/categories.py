from fastapi import APIRouter, HTTPException
from database import SessionLocal
from models import Category
from pydantic import BaseModel


router = APIRouter()


class WriteCategoryBase(BaseModel):
    name : str

@router.get('/api/categories', tags=["Category"])
def read_all_categories():
    db = SessionLocal()
    db_categories =  db.query(Category).all()
    
    return db_categories



@router.get('/api/category/{category_id}', tags=["Category"])
def read_category(category_id : int):
    db = SessionLocal()
    db_category =   db.query(Category).filter(Category.id == category_id).first()
    return db_category


@router.post("/api/category", tags=["Category"])
def write_category(new_category : WriteCategoryBase):
    db = SessionLocal()
    db_new_category = Category(name= new_category.name)
    db.add(db_new_category)
    db.commit()
    db.refresh(db_new_category)
    return {"message" : "Category created successfully"}

@router.delete("/api/category/{category_id}", tags=["Category"])
def delete_category(category_id : int):
    db = SessionLocal()
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if db_category is None :
        raise HTTPException(statuc_code=404, detail="Category not found")
    db.delete(db_category)
    db.commit()
    
    return {"message" : "Category deleted succcesfully"}



    