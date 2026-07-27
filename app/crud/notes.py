from sqlalchemy.orm import Session
from app import models
from app.schemas.note import *
from typing import List
from app.models.note import Note
from typing import Optional



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



# Pagination
def get_notes(db: Session, user_id: int, skip: int, limit: int) -> List[Note]:
    return(
        db.query(Note)
        .filter(Note.user_id == user_id)
        .order_by(Note.created_at.desc())
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