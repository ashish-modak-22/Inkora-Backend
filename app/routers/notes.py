from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.models.note import Note
from app.schemas.note import NoteCreate, NoteResponse
from app.crud.notes import create_note as create_note_db, get_notes



router = APIRouter(prefix="/notes", tags=["Notes"])


# Creating a new note for the authenticated user
@router.post("/", response_model=NoteResponse)
async def create_note_route(
    note: NoteCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return create_note_db(
        db = db,
        note = note,
        user_id = current_user.id
    )