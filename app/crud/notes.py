from sqlalchemy.orm import Session
from app import models
from app.schemas import note
from typing import List
from app.models.note import Note



def create_note(db: Session, note: note.NoteCreate, user_id: int):

    db_note = models.Note(
        title = note.title,
        content = note.content,
        user_id = user_id
    )

    db.add(db_note)
    db.commit()
    db.refresh(db_note)

    return db_note


def get_notes(db: Session, user_id: int) -> List[Note]:
    return (
        db.query(Note)
        .filter(Note.user_id == user_id)
        .order_by(Note.created_at.desc())
        .all()
    )