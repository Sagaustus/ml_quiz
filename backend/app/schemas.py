from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str
    full_name: str | None = None
    profile_pic: str | None = None

class User(UserBase):
    id: int
    full_name: str | None = None
    profile_pic: str | None = None

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None
