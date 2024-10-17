# models.py
from sqlalchemy import Column, Integer, String, Text, DateTime
from .database import Base

class TelegramMessage(Base):
    __tablename__ = 'telegram_messages'
    
    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, index=True)
    message = Column(Text)
    sender_id = Column(Integer)
    timestamp = Column(DateTime)
    status_description = Column(String)
    
    # Add more columns as per your data requirements
