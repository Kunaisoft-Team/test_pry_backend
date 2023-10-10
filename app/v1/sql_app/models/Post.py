from sqlalchemy import Column, Integer, String,ForeignKey,Text
from sqlalchemy.orm import relationship


from app.v1.sql_app import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    content = Column(Text(), index=True)

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="posts")