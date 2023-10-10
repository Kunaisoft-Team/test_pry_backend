from  sqlalchemy.orm import Session
from .models import Post,User
from app.v1.schemas import Post as PostSchema,UserCreate
from passlib.context import CryptContext
from fastapi import HTTPException




def get_user(db: Session,user_id:int):
    try:
        return db.query(User).filter(User.id == user_id).first()
    except Exception as e:
        return HTTPException(status_code=400,detail="User not found")


def create_user(db:Session,user:UserCreate,new_password:str):


    try :
        db_user = User(name=user.name,lastname=user.lastname,email=user.email,hashed_password=new_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        return HTTPException(status_code=400,detail="Email already exists")


def get_posts(db:Session,user:User,skip:int = 0,limit:int = 100,):
    try:
        return db.query(Post).filter(User.id == user.id).offset(skip).limit(limit).all()
    except Exception as e:
        return HTTPException(status_code=400,detail="Error getting posts")


def get_post(db:Session,id:int,user:User):
    try:
        return db.query(Post).filter((Post.id == id) & (User.id == user.id)).first()
    except Exception as e:
        return HTTPException(status_code=400,detail="Post not found")


def delete_post(db:Session,id:int,user:User):
    try:
        db_post = db.query(Post).filter((Post.id == id) & (User.id == user.id)).first()
        db.delete(db_post)
        db.commit()
        return db_post
    except Exception as e:
        return HTTPException(status_code=400,detail="Post not found")


def create_user_post(db: Session, item: PostSchema,user_id: int):
    try:
        db_item = Post(**item.model_dump(),owner_id=user_id)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    except Exception as e:
        return HTTPException(status_code=400,detail="Failed to create post")
