from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.v1.settings import Env

env = Env()

SQLALCHEMY_DATABASE_URL = f"mysql://{env.MYSQL_USER}:{env.MYSQL_PASSWORD}@{env.MYSQL_HOST}/{env.MYSQL_DB}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()