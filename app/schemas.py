from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# ─── POST SCHEMAS ─────────────────────────────

class PostBase(BaseModel):
    title: str              # post title
    body: str               # post content
    published: bool = True  # default = True
    rating: Optional[int] = None      # post rating

class PostCreate(PostBase):
    pass  # used when creating a post (same fields as base)

class PostUpdate(PostBase):
    pass  # used when updating a post (same fields)

# ─── USER SCHEMAS ─────────────────────────────

class UserCreate(BaseModel):
    username: str
    email: EmailStr   # automatically checks valid email
    password: str
    phone: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    phone: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True  # ORM → schema conversion


class Token(BaseModel):
    access_token: str
    refresh_token: Optional[str] = None
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None


class OwnerInfo(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True

class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: Optional[int] = None
    owner: Optional[OwnerInfo] = None   # ← YANGI

    class Config:
        from_attributes = True

class Passwordchange(BaseModel):
    old_password: str
    new_password: str