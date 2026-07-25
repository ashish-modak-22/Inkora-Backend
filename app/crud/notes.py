from sqlalchemy.orm import Session
from app import models
from app.schemas.note import NoteCreate



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