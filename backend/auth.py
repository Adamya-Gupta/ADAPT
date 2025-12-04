from typing import Annotated
from fastapi.params import Depends
from passlib.context import CryptContext
from sqlmodel import Session , select
from backend.db import get_session
from backend.models import User , SingleFile

# pwd_context = CryptContext(schemes="bcrypt")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password):
    return pwd_context.hash(password)

def get_user_from_db(session: Annotated[Session,
                    Depends(get_session)], 
                     username:str | None = None, 
                     email:str | None = None):
    statement = select(User).where(User.username == username)
    user = session.exec(statement).first()
    print(user)
    
    # check by email if not found by username
    if not user:
        statement = select(User).where(User.email == email)
        user = session.exec(statement).first()
        if user:
            return user
    return user