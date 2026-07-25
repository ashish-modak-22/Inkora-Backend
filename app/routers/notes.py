from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.models.note import Note
from app.schemas.note import NoteCreate, NoteResponse



router = APIRouter(prefix="/notes", tags=["Notes"])


# Creating a new note for the authenticated user
@router.post("/", response_model=NoteResponse)
async def create_note(
    note: NoteCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    # Object to create a new note linked to the authenticated user
    new_note = Note(
        title = note.title,
        content = note.content,
        user_id = current_user.id
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note