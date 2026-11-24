# id (PK)	UUID
# name	VARCHAR(150)
# equipment	VARCHAR(50)
# movement_type	VARCHAR(30)
# tracking_type	VARCHAR(30)
# instructions	TEXT
# created_by_user_id (FK → users)	UUID, nullable
# is_public	BOOLEAN
# created_at	TIMESTAMP

from sqlalchemy import Column, Integer, String, Text, ForeignKey, VARCHAR, TIMESTAMP, Enum as SAEnum
# from sqlalchemy.orm import relationship
from app.backend.config.config import Base
import enum

class Exercise(Base):
    __tablename__ = "exercise"

    id = Column(Integer, unique=True, primary_key=True, nullable=False, index=True)
    name = Column(VARCHAR(255), unique=True, nullable=False)
    equipment = Column(VARCHAR(50), nullable=False)
    movement_type = Column(VARCHAR(50), nullable=False)
    tracking_type = Column(VARCHAR(30), nullable=False)
    instructions = Column(Text, nullable=True)
    created_by_user_id = Column(ForeignKey("users_table.id"), nullable=False)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)