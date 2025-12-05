from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi.params import Depends
from passlib.context import CryptContext
from sqlmodel import Session , select
from backend.db import get_session
from backend.models import User , SingleFile
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError , jwt

SECRET_KEY = 'ad8d636d00404cc47941df11fea0bc719b6387ffbdd7fcd90dc93d2e0f7fa13b'
ALGORITHM = 'HS256'
EXPIRY_TIME = 30 # minutes

# Login token URL
oauth_scheme = OAuth2PasswordBearer(tokenUrl="/token")

# pwd_context = CryptContext(schemes="bcrypt")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(password, hash_password):
    return pwd_context.verify(password, hash_password)

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

def authenticate_user(
        username: str,
        password: str,
        session: Annotated[Session, Depends(get_session)]
):
    db_user = get_user_from_db(session, username = username)
    if not db_user:
        return False
    if not verify_password(password=password, hash_password=db_user.password):
        return False
    return db_user

def create_access_token(data:dict,expiry_time:timedelta|None):
    data_to_encode = data.copy()
    if expiry_time:
        expire = datetime.now(timezone.utc) + expiry_time
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    data_to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(data_to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt 