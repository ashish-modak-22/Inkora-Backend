from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.models.note import Note
from app.schemas.note import NoteCreate, NoteResponse, NoteUpdate
from app.crud.notes import create_note as create_note_db, get_notes, get_note_by_id, update_note, delete_note



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



# Router for getting all notes
# @router.get("/", response_model=list[NoteResponse])
# async def get_all_notes(
#     current_user: User = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     return get_notes(
#         db=db,
#         user_id=current_user.id
#     )



@router.get("/", response_model=list[NoteResponse])
async def get_all_notes(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    search: str | None = None,
    sort_by: str = Query("created_at", pattern="^(created_at|title)$"),
    order: str = Query("desc", pattern="^(asc|desc)$")
):

    skip = (page-1)*limit

    return get_notes(
        db=db,
        user_id = current_user.id,
        skip=skip,
        limit=limit,
        search=search,
        sort_by=sort_by,
        order=order
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
            detail="Note not found"
        )

    return note



@router.put("/{note_id}", response_model=NoteResponse)
async def update_note_route(
    note_id: int,
    note: NoteUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    db_note = get_note_by_id(
        db = db,
        note_id = note_id,
        user_id = current_user.id
    )

    if not db_note:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    return update_note(
        db=db,
        db_note = db_note,
        note = note
    )



@router.delete("/{note_id}")
async def delete_note_route(
    note_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    db_note = get_note_by_id(
        db=db,
        note_id=note_id,
        user_id=current_user.id
    )

    if not db_note:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    delete_note(
        db=db,
        db_note=db_note
    )

    return {
        "message": "Note deleted successfully"
    }