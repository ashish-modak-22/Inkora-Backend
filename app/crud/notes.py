from sqlalchemy.orm import Session
from app import models
from app.schemas.note import *
from typing import List
from app.models.note import Note
from typing import Optional
from sqlalchemy import or_



def create_note(db: Session, note: NoteCreate, user_id: int):

    db_note = models.Note(
        title = note.title,
        content = note.content,
        user_id = user_id
    )

    db.add(db_note)
    db.commit()
    db.refresh(db_note)

    return db_note



# Used to get all notes in list  
# def get_notes(db: Session, user_id: int) -> List[Note]:
#     return (
#         db.query(Note)
#         .filter(Note.user_id == user_id)
#         .order_by(Note.created_at.desc())
#         .all()
#     )



# Pagination + searching for notes + Sorting support
def get_notes(db: Session, user_id: int, skip: int, limit: int, search: Optional[str]=None, sort_by: str = "created_at", order: str = "desc") -> List[Note]:

    query = (
        db.query(Note)
        .filter(Note.user_id == user_id)
    )

    if search:
        query = query.filter(
            or_(
                Note.title.ilike(f"%{search}%"),
                Note.content.ilike(f"%{search}%")
            )
        )

    if sort_by == "title":
        sort_column = Note.title

    else:
        sort_column = Note.created_at

    if order.lower() == "asc":
        query = query.order_by(sort_column.asc())

    else:
        query = query.order_by(sort_column.desc())

    return(
        query
        .offset(skip)
        .limit(limit)
        .all()
    )



def get_note_by_id(db: Session, note_id: int, user_id: int) -> Optional[Note]:
    return (
        db.query(Note).filter(
            Note.id == note_id,
            Note.user_id == user_id
        ).first()
    )



def update_note(db: Session, db_note: Note, note: NoteUpdate) -> Note:

    db_note.title = note.title
    db_note.content = note.content

    db.commit()
    db.refresh(db_note)

    return db_note



def delete_note(
    db: Session,
    db_note: Note
) -> None:

    db.delete(db_note)
    db.commit()