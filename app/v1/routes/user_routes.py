from fastapi import APIRouter
from fastapi import Depends,Body

from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi import HTTPException,status

from app.v1.sql_app import create_user,get_user
from app.v1.schemas import UserCreate,User
from app.v1.controllers import auth_controller
from app.v1.sql_app import get_db
from app.v1.schemas.Token import Token
router = APIRouter()




@router.post("/signup",
status_code=status.HTTP_201_CREATED,response_model=User,
tags=["users"]
)
async def signup(user:UserCreate = Body, db:Session = Depends(get_db)):
    new_password = auth_controller.get_password_hash(user.password)
    return auth_controller.generate_token(user.email,new_password,db=db)





@router.post("/login",tags=["users"],response_model=Token,status_code=status.HTTP_200_OK)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db:Session = Depends(get_db)
):
    token = auth_controller.generate_token(form_data.username,form_data.password,db=db)
    (token)
    return  Token(access_token=token,token_type="bearer")