from datetime import datetime,timedelta
from typing import Optional
from fastapi import Depends, HTTPException,status

from fastapi.security import OAuth2PasswordBearer

from jose import JWTError,jwt
from passlib.context import CryptContext

from app.v1.sql_app.models import User
from app.v1.schemas.Token import TokenData
from app.v1.settings import Env
from sqlalchemy.orm import Session
from app.v1.sql_app import get_db

settings = Env()

SECRET_KEY = settings.secret_key

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = settings.token_expire

pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

oauth2_sheme = OAuth2PasswordBearer(tokenUrl="api/v1/login")


def verify_password(plain_password,password):
    return pwd_context.verify(plain_password,password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db:Session,email:str) -> User:
    return db.query(User).filter((User.email == email)).first()

def authenticate_user(email:str,password:str,db:Session):
    user = get_user(email=email,db=db)

    if not user:
        return False

    if not verify_password(password,user.hashed_password):
        return False

    return user


def create_access_token(data:dict,expires_delta:Optional[timedelta] = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({'exp':expire})
    encode_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encode_jwt

def generate_token(email,password,db:Session):
    user = authenticate_user(email,password,db=db)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorret email or password",
            headers={"WWW-Authenticate":"Bearer"}
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    return create_access_token(
        data={"sub":user.email},expires_delta=access_token_expires
    )

async def get_current_user(db=Depends(get_db),token:str = Depends(oauth2_sheme)):

    (token)

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate":"Bearer"}
    )

    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        (payload)
        email : str = payload.get("sub")
        (email)
        if email is None:
            raise credentials_exception

        token_data = TokenData(email=email)

    except JWTError as error:
        raise credentials_exception

    user = get_user(db,email=token_data.email)

    if user is None:
        raise credentials_exception

    return user