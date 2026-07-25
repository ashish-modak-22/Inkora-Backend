from datetime import datetime
from pydantic import BaseModel, ConfigDict



class NoteCreate(BaseModel):
    title: str
    content: str


class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

    # Conversion from SQLAlchemy model to Pydantic model
    model_config = ConfigDict(
        from_attributes=True
    )