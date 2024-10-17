# schemas.py
from pydantic import BaseModel
from datetime import datetime

class TelegramMessageBase(BaseModel):
    source: str
    message: str
    sender_id: int
    timestamp: datetime
    status_description: str

class TelegramMessageCreate(TelegramMessageBase):
    pass

class TelegramMessage(TelegramMessageBase):
    id: int
    
    class Config:
        orm_mode = True
