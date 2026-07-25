from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy.orm import relationship




class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)

    # One user multiple notes
    notes = relationship("Note", back_populates="owner", cascade="all, delete-orphan")