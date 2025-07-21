from pydantic import BaseModel, EmailStr
from enum import Enum

class RoleEnum(str, Enum):
    sensei = "sensei"
    karateka = "karateka"

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None
    role: RoleEnum = RoleEnum.karateka

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    id: int
    is_active: bool

    model_config = {
    "from_attributes": True
}

class UserOut(UserInDB):
    pass

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    username: str | None = None
