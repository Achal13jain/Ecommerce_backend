from pydantic import BaseModel, EmailStr, Field
from typing import Literal

class UserCreate(BaseModel):
    name: str= Field(..., min_length=3,max_length=30)
    email: EmailStr
    password: str= Field(..., min_length=6)
    role: Literal["admin", "user"]  # Restrict role to allowed values

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class ForgotPasswordRequest(BaseModel):
    email: EmailStr

class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str= Field(..., min_length=6)
