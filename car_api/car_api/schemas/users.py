from pydantic import BaseModel, EmailStr

class UserScreen(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserPublicSchema(BaseModel):
    id: int
    username: str
    email: EmailStr