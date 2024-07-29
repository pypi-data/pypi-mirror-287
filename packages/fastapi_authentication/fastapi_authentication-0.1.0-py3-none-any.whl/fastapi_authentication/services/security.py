
from datetime import datetime, timedelta
from typing import Annotated
from fastapi import Depends, HTTPException, status
from passlib.context import CryptContext
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi_authentication import models
from fastapi_authentication.config import ALGORITHM, SECRET_KEY
from fastapi_authentication.con import db_dependency

secret_key = SECRET_KEY
algorithm = ALGORITHM


bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')


# step 1: authenticate user
def authenticate_user(username_or_email: str, password: str, db: db_dependency):
    # Check if the input is an email or username based on the presence of '@'
    if '@' in username_or_email:
        user = db.query(models.User).filter(
            models.User.email == username_or_email).first()
    else:
        user = db.query(models.User).filter(
            models.User.username == username_or_email).first()

    if user and bcrypt_context.verify(password, user.hashed_password):
        return user
    return None


# step 2: create access token
def create_access_token(username: str, user_id: int):
    access_token_expires = timedelta(minutes=15)
    refresh_token_expires = timedelta(days=7)

    access_token = jwt.encode(
        {"sub": username, "id": user_id, "exp": datetime.utcnow() +
         access_token_expires},
        SECRET_KEY, algorithm=ALGORITHM)

    refresh_token = jwt.encode(
        {"sub": username, "id": user_id, "exp": datetime.utcnow() +
         refresh_token_expires},
        SECRET_KEY, algorithm=ALGORITHM)

    return access_token, refresh_token


# step 3: get current user
async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="could not validate user")
        return {"username": username, "id": user_id, }
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="could not validate user")


user_dependency = Annotated[dict, Depends(get_current_user)]


def generate_username(email, first_name, last_name):
    # Simple example: use part of the email or first and last name
    # You can make this more sophisticated to ensure uniqueness
    username_base = email.split('@')[0]
    return f"{username_base}_{first_name.lower()}"
