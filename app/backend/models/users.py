from sqlalchemy import Column, Integer, String, Text, ForeignKey, VARCHAR, TIMESTAMP, Enum as SAEnum
# from sqlalchemy.orm import relationship
from app.backend.config.config import Base
import enum

class weights_unit(enum.Enum):
    KG = "kg"
    LBS = "lbs"

class status(enum.Enum):
    INACTIVE = "inactive"
    ACTIVE = 'active'

class User(Base):
    __tablename_ = "users_table"

    id = Column(Integer, unique=True, primary_key=True, index=True)
    email = Column(VARCHAR(255), unique=True, nullable=False)
    password = Column(VARCHAR(255), nullable=False)
    name = Column(VARCHAR(255), nullable=False)
    preffered_weight_unit = Column(SAEnum(weights_unit), default=weights_unit.KG, nullable=False)
    status = Column(SAEnum(status, name = "STATUS"))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)


#WHEN USER IS FIRST CREATED BYDEFAULT IT SHOULD BE ACTIVE
#LOOK FOR ENUM IN FASTAPI