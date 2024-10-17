# crud.py
from sqlalchemy.orm import Session
from . import models, schemas

def get_messages(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.TelegramMessage).offset(skip).limit(limit).all()

def create_message(db: Session, message: schemas.TelegramMessageCreate):
    db_message = models.TelegramMessage(**message.dict())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message
