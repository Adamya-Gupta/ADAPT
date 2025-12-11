from datetime import timedelta
from fastapi import FastAPI , Depends , HTTPException , status
from sqlmodel import Session ,select
from typing import Annotated
from contextlib import asynccontextmanager
from backend.auth import EXPIRY_TIME, authenticate_user, create_access_token, create_access_token , current_user, validate_refresh_token , create_refresh_token
from backend.db import get_session,create_tables
from backend.models import SingleFile, SingleFile_Create, SingleFile_Edit, Token, User
from backend.router import user
from fastapi.security import OAuth2PasswordRequestForm

# First task after starting of the app should be to create tables
@asynccontextmanager
async def lifespan(app:FastAPI):
    print('Creating Tables')
    create_tables()
    print('Tables Created')
    yield

app :FastAPI = FastAPI(lifespan=lifespan,title="SingleFile",version='1.0.0')

app.include_router(router=user.user_router)

@app.get('/')
async def root():
    return {"message" : "Welcome to the fastapi server"}

# Login
@app.post('/token',response_model=Token)
async def login(form_data:Annotated[OAuth2PasswordRequestForm,Depends()],
                session:Annotated[Session,Depends(get_session)]):
    user = authenticate_user(form_data.username,
                             form_data.password,
                             session)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )
    
    expire_time = timedelta(minutes=EXPIRY_TIME)
    access_token = create_access_token({"sub":form_data.username},expire_time)

    refresh_expire_time = timedelta(days=7)
    refresh_token = create_refresh_token({"sub":user.email},refresh_expire_time)


    return Token(access_token=access_token,token_type="bearer",
                 refresh_token=refresh_token)


@app.post('/token/resfresh')
def refresh_token(old_refresh_token: str,
                  session:Annotated[Session,Depends(get_session)]):
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail="Invalid token, Please login again",
        headers={"www-Authenticate":"Bearer"},
    )
    user = validate_refresh_token(old_refresh_token,session)

    if not user:
        raise credentials_exception


    expire_time = timedelta(minutes=EXPIRY_TIME)
    access_token = create_access_token({"sub":user.username},expire_time)

    refresh_expire_time = timedelta(days=7)
    refresh_token = create_refresh_token({"sub":user.email},refresh_expire_time)

    return Token(access_token=access_token,token_type="bearer",refresh_token=refresh_token)

# injected session dependency 
@app.post('/contents/',response_model=SingleFile)
async def create_content(current_user:Annotated[User,Depends(current_user)],
                          file : SingleFile_Create , 
                          session:Annotated[Session,Depends(get_session)]):
    
    new_file = SingleFile(
        content = file.content,
        user_id = current_user.id
    )

    session.add(new_file)
    session.commit()
    session.refresh(new_file)
    return new_file

@app.get('/contents/',response_model= list[SingleFile])
async def get_all(
    current_user:Annotated[User,Depends(current_user)],
    session:Annotated[Session,Depends(get_session)]):

    allfiles = session.exec(select(SingleFile).where(SingleFile.user_id == current_user.id)).all()

    # even if no files found return empty list

    return allfiles

@app.get('/contents/{id}',response_model=SingleFile)
async def get_single_content(id: int, 
                             current_user:Annotated[User,Depends(current_user)],
                             session:Annotated[Session,Depends(get_session)]):
    
    user_files = session.exec(select(SingleFile).where(SingleFile.user_id == current_user.id)).all()
    matched_files = next((file for file in user_files if file.id == id), None)
    
    # singlefile = session.get(SingleFile,id)
    if matched_files:
        return matched_files
    else:
        raise HTTPException (status_code=404 , detail="No file found")
        

@app.put('/contents/{id}')
async def edit_content(id:int,
                       file:SingleFile_Edit,
                        current_user:Annotated[User,Depends(current_user)],
                       session:Annotated[Session,Depends(get_session)]):
    
    user_files = session.exec(select(SingleFile).where(SingleFile.user_id == current_user.id)).all()
    existingfile = next((file for file in user_files if file.id == id), None)

    if existingfile:
        existingfile.content = file.content
        existingfile.doc_type = file.doc_type
        existingfile.is_edited = True

        session.add(existingfile)
        session.commit()
        session.refresh(existingfile)
        return existingfile
    else:
        raise HTTPException (status_code=404 , detail="No content found")

@app.delete('/contents/{id}')
async def delete_content(id:int,
                          current_user:Annotated[User,Depends(current_user)],
                          session:Annotated[Session,Depends(get_session)] ):
    
    user_files = session.exec(select(SingleFile).where(SingleFile.user_id == current_user.id)).all()
    file = next((file for file in user_files if file.id == id), None)

    if file:
        session.delete(file)
        session.commit()
        return {"Message : file deleted successfully"}
    else:
        raise HTTPException (status_code=404 , detail="No content found")
