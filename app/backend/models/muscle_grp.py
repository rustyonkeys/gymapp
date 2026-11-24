from sqlalchemy import Column, Integer, String, Text, ForeignKey, VARCHAR, TIMESTAMP, Enum as SAEnum
# from sqlalchemy.orm import relationship
from app.backend.config.config import Base

class MuscleGroup(Base):
    __tablename__ = "muscle_group"

    id = Column(Integer, unique=True, primary_key=True, index=True)
    name = Column(VARCHAR(255), nullable=False, unique= True)
    parent_id = Column(Integer,ForeignKey("muscle_group.id"), nullable=True)