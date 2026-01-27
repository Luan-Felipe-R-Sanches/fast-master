from typing import List, Optional
from pydantic import BaseModel, EmailStr

class UserScreen(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserPublicSchema(BaseModel):
    id: int
    username: str
    email: EmailStr

class UserUpdateSchema(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

class UserListPublicSchema(BaseModel):
    users: List[UserPublicSchema]