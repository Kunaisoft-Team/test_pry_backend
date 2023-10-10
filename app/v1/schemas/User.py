from .Base import Base
from pydantic import Field
from .Post import Post

class UserBase(Base):
    name:str = Field(..., example="John Doe")
    lastname:str = Field(..., example="Doe")
    email: str = Field(..., example="example@gmail.com")


class UserCreate(UserBase):
    password: str = Field(..., example="wiiiii")

class User(UserBase):
    id:int
    posts: list[Post] = []