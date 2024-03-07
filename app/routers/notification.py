from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User, Admin, Notification
from pydantic import BaseModel
from typing import List
from sqlalchemy import desc
from fastapi import HTTPException, status


router = APIRouter()

class WriteNotificationBase(BaseModel):
    id : str
    contest_id : int
    title : str
    description : str
    
class UpdateNotificationBase(BaseModel):
    title : str | None = None
    description : str | None = None
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        

@router.get("/api/notification", tags=["Notification"])
def read_all_notifications(db: Session = Depends(get_db)):
    notifications = db.query(Notification).order_by(desc(Notification.created_at)).all()
    return notifications

@router.get("/api/contest/{contest_id}/notification", tags=["Notification", "Contest"])
def read_all_notifications_by_contest_id(contest_id : int, db: Session = Depends(get_db)):
    
    notifications = db.query(Notification).filter(Notification.contest_id == contest_id).order_by(desc(Notification.created_at)).all()
    if not notifications:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Notifications not found")
    return notifications

@router.get("/api/notification/{notification_id}", tags=["Notification"])
def read_notification(notification_id : int, db: Session = Depends(get_db)):
    notification = db.query(Notification).filter(Notification.id == notification_id).first()
    if notification is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Notification not found")
    return notification


@router.post("/api/notification", tags=["Notification"])
def write_notification(new_notification : WriteNotificationBase, db: Session = Depends(get_db)):
    db_new_notification = Notification(id = new_notification.id, contest_id = new_notification.contest_id, title = new_notification.title, description = new_notification.description)
    db.add(db_new_notification)
    db.commit()
    db.refresh(db_new_notification)
    return {"message" : "Notification created successfully"}

@router.put("/api/notification/{notification_id}", tags=["Notification"])
def update_notification(notification_id: int, notification_data: UpdateNotificationBase, db: Session = Depends(get_db)):
    notification = db.query(Notification).filter(Notification.id == notification_id).first()
    if not notification:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Notification not found")
    if notification_data.title is not None:
        notification.title = notification_data.title
    if notification_data.description is not None:
        notification.description = notification_data.description
    db.add(notification)
    db.commit()
    return {"message": "Notification updated successfully"}

@router.delete("/api/notification/{notification_id}", tags=["Notification"])
def delete_notification(notification_id: int, db: Session = Depends(get_db)):
    notification = db.query(Notification).filter(Notification.id == notification_id).first()
    if not notification:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Notification not found")
    db.delete(notification)
    db.commit()
    return {"message": "Notification deleted successfully"}


