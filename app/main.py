# To run the main file on local network: "uvicorn app.main:app --reload"
# To run the main file on any network: "python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"



from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserRegister, UserResponse
from app.models.user import User
from fastapi import HTTPException
from app.core.security import hash_password
from app.routers import auth
from app.routers import notes




app  = FastAPI()


app.include_router(auth.router)
app.include_router(notes.router)


# Root endpoint that is called when the base URL ("/") is accessed
@app.get("/")
def home():

    # Return a welcome message in JSON format
    return {
        "message": "Welcome to NotesApp Backend"
    }
