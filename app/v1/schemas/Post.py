from .Base import Base
from pydantic import Field

class PostBase(Base):
    title:str = Field(...,example="this is a title")
    content:str | None = Field(default=None,example="this is a post")


class PostCreate(PostBase):
    pass

class Post(PostBase):
    id:int