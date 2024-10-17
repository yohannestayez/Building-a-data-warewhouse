# main.py
import sys
sys.path.append("C:/Users/Administrator/Documents/kifiya/Week_7/App")
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import engine, get_db
from fastapi import FastAPI
from fastapi.responses import FileResponse

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Telegram Messages API"}

# Read messages
@app.get("/messages/", response_model=list[schemas.TelegramMessage])
def read_messages(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    messages = crud.get_messages(db=db, skip=skip, limit=limit)
    return messages

# Create message
@app.post("/messages/", response_model=schemas.TelegramMessage)
def create_message(message: schemas.TelegramMessageCreate, db: Session = Depends(get_db)):
    return crud.create_message(db=db, message=message)

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("App/favicon.ico")