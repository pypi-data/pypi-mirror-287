from typing import Annotated
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi_authentication.config import SQLALCHEMY_DATABASE_URL
# from .config import SQLALCHEMY_DATABASE_URL


engine = create_engine(SQLALCHEMY_DATABASE_URL)
                       
SessionLocal = sessionmaker(bind=engine)


Base = declarative_base()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]  # Use Session class here
