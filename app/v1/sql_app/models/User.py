from sqlalchemy import Column, Integer, String,Boolean
from sqlalchemy.orm import relationship
from app.v1.sql_app import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    lastname = Column(String(100), index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)


    posts = relationship("Post", back_populates="owner")