from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.models.note import Note
from app.schemas.note import NoteCreate, NoteResponse
from app.crud.notes import create_note as create_note_db, get_notes, get_note_by_id



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



@router.get("/", response_model=list[NoteResponse])
async def get_all_notes(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return get_notes(
        db=db,
        user_id=current_user.id
    )



@router.get("/{note_id}", response_model=NoteResponse)
async def get_note(
    note_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    note = get_note_by_id(
        db=db,
        note_id=note_id,
        user_id=current_user.id
    )

    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note note found"
        )

    return note