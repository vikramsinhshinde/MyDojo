from sqlalchemy import Column, Integer, String, Boolean, Enum
from app.db.base import Base
import enum

class RoleEnum(str, enum.Enum):
    sensei = "sensei"
    karateka = "karateka"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    role = Column(Enum(RoleEnum), default=RoleEnum.karateka)
