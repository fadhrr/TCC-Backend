from fastapi import APIRouter, Depends, Path, Query, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from ..database import SessionLocal
from ..models import Problem, ProblemCategory, Category
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.orm import Session
from fastapi import Depends
 
router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def format_category_name(problem, db : Session = Depends(get_db)):
    categories_id = problem.categories
    categories_name = []
    for category_id in categories_id:
        category_name = db.query(Category).filter(Category.id == category_id.id).first().name
        categories_name.append(category_name)
    problem.categories = categories_name
    return problem


class WriteProblemBase(BaseModel):
    title : str
    description : str
    time_limit : int
    memory_limit : int
    input_format : str
    sample_input : str
    output_format : str
    sample_output : str
    constraints : str
    explanation : str | None = None
    category : list[int] 

class UpdatedProblemBase(BaseModel):
    title : str | None = None
    description : str | None = None
    time_limit : int | None = None
    memory_limit : int | None = None
    input_format : str | None = None
    sample_input : str | None = None
    output_format : str | None = None
    sample_output : str | None = None
    constraints : str | None = None
    explanation : str | None = None
    category : list[int] | None = None  
    
@router.get('/api/problems', tags=["Problem"])
def read_problems(db: Session = Depends(get_db)):
    
    
    db_problems = db.query(Problem).options(joinedload(Problem.categories)).all()
    return db_problems
    
@router.get("/api/problems/search", tags=["Problem"])
def search_problem(q : str | None = None,db: Session = Depends(get_db)):
    
    
    items = db.query(Problem).filter(Problem.title.contains(q)).all()
    return items

@router.get('/api/problem/{problem_id}', tags=["Problem"])
def read_problem(problem_id : int,db: Session = Depends(get_db)):
    
    
    db_problem = db.query(Problem).options(joinedload(Problem.categories)).filter(Problem.id == problem_id).first()
    if db_problem is None :
        raise HTTPException(status_code=404, detail="Problem not found")
    return db_problem


@router.post('/api/problem', tags=["Problem"])
def create_problem(new_problem : WriteProblemBase,db: Session = Depends(get_db)):
    
    
    problem = Problem(
        title = new_problem.title,
        description = new_problem.description,
        time_limit = new_problem.time_limit,
        memory_limit = new_problem.memory_limit,
        input_format = new_problem.input_format,
        sample_input = new_problem.sample_input,
        output_format = new_problem.output_format,
        sample_output = new_problem.sample_output,
        constraints = new_problem.constraints
        )
    for category_id in new_problem.category:
        category = db.query(Category).filter(Category.id == category_id).first()
        if category is None:
            raise HTTPException(status_code=404, detail="Category not found")
        problem.categories.append(category)
        
        
    if new_problem.explanation is not None :
        problem.explanation = new_problem.explanation

    db.add(problem)
    db.commit()
    db.refresh(problem)
    
    db_problem = db.query(Problem).options(joinedload(Problem.categories)).filter(Problem.id == problem.id).first()
    if db_problem is None :
        raise HTTPException(status_code=404, detail="Problem not found")
    db_problem = format_category_name(db_problem, db)
    return {"message": "Problem retrieved successfully",
            "data": db_problem}

@router.put('/api/problem/{problem_id}', tags=["Problem"])
def update_problem(problem_id : int, new_problem : UpdatedProblemBase,db: Session = Depends(get_db)):
    
    
    old_problem = db.query(Problem).filter(Problem.id == problem_id).first()
    
    if not old_problem :
        raise HTTPException(status_code=404, detail="Problem not found")

    if new_problem.title is not None :
        old_problem.title = new_problem.title
    
    if new_problem.description is not None :
        old_problem.description = new_problem.description
    
    if new_problem.time_limit is not None :
        old_problem.time_limit = new_problem.time_limit
    
    if new_problem.memory_limit is not None :
        old_problem.memory_limit = new_problem.memory_limit
    
    if new_problem.input_format is not None :
        old_problem.input_format = new_problem.input_format
    
    if new_problem.sample_input is not None :
        old_problem.sample_input = new_problem.sample_input
    
    if new_problem.output_format is not None :
        old_problem.output_format = new_problem.output_format
    
    if new_problem.sample_output is not None :
        old_problem.sample_output = new_problem.sample_output
    
    if new_problem.constraints is not None :
        old_problem.constraints = new_problem.constraints
    
    if new_problem.explanation is not None :
        old_problem.explanation = new_problem.explanation
    
    db.add(old_problem)
    db.commit()
    
    return { "message" : "Problem updated successfully"}

@router.delete('/api/problems/{problem_id}', tags=["Problem"])
def function(problem_id : int,db: Session = Depends(get_db)):
    problem = db.query(Problem).filter(Problem.id==problem_id).first()
    if problem is None :
        raise HTTPException(status_code=404, detail="Problem was not found")
    db.delete(problem)
    db.commit()
    
    return {"message" : "Problem deleted successfully"}
    
# @router.get('/api/problems/categories/{category_name}', tags=["problems", "categories"])
# def read_problem_categories(category_name : str):
#     
    
#     category = db.query(Category).filter(Category.name == category_name).first()
#     if category_id is None :
#         raise HTTPException(status_code=404, detail="Category not found")
    
#     db_problem = db.query(Problem).options(joinedload(Problem.categories)).all()
#     if db_problem is None :
#         raise HTTPException(status_code=404, detail="Problem not found")
#     # db_categories = db_problem.categories
#     return db_problem


# get router based on category
@router.get('/api/problems/categories/{category_id}', tags=["Problem", "Category"])
def read_problem_category(category_id : int,db: Session = Depends(get_db)):
    
    
    db_problem = db.query(Problem).join(ProblemCategory).filter(ProblemCategory.category_id == category_id).all()
    if db_problem is None :
        raise HTTPException(status_code=404, detail="Problem not found")
    return db_problem

@router.post("/api/problems/{problem_id}/categories/{category_id}", tags=["Problem", "Category"])
def add_problem_category(problem_id : int, category_id : int, db: Session = Depends(get_db)):
    problem = db.query(Problem).filter(Problem.id == problem_id).first()
    category = db.query(Category).filter(Category.id == category_id).first()
    if problem is None or category is None:
        raise HTTPException(status_code=404, detail="Problem or Category not found")
    try:
        new_problem_category = ProblemCategory(problem_id = problem_id, category_id = category_id)
        db.add(new_problem_category)
        db.commit()
        return {"message" : "Category added successfully", "data" : new_problem_category}
    except:
        raise HTTPException(status_code=400, detail="Problem already has this category")
        
@router.delete("/api/problems/{problem_id}/categories/{category_id}", tags=["Problem", "Category"])
def delete_problem_category(problem_id : int, category_id : int, db: Session = Depends(get_db)):
    problem_category = db.query(ProblemCategory).filter(ProblemCategory.problem_id == problem_id, ProblemCategory.category_id == category_id).first()
    if problem_category is None:
        raise HTTPException(status_code=404, detail="Problem or Category not found")
    db.delete(problem_category)
    db.commit()
    return {"message" : "Category from problem deleted successfully"}

