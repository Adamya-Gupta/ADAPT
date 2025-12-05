from fastapi import FastAPI , Depends , HTTPException
from sqlmodel import Session ,select
from typing import Annotated
from contextlib import asynccontextmanager
from backend.auth import authenticate_user
from backend.db import get_session,create_tables
from backend.models import SingleFile
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
@app.post('/token')
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
    return user

# injected session dependency 
@app.post('/contents/',response_model=SingleFile)
async def create_content(file : SingleFile , session:Annotated[Session,Depends(get_session)]):
    session.add(file)
    session.commit()
    session.refresh(file)
    return file

@app.get('/contents/',response_model= list[SingleFile])
async def get_all(session:Annotated[Session,Depends(get_session)]):
    statement = select(SingleFile)
    allfiles = session.exec(statement).all()

    # even if no files found return empty list
    return allfiles

@app.get('/contents/{id}',response_model=SingleFile)
async def get_single_content(id: int, session:Annotated[Session,Depends(get_session)]):
    # singlefile = session.exec(select(SingleFile).where(SingleFile.id == id)).first()
    singlefile = session.get(SingleFile,id)
    if singlefile:
        return singlefile
    else:
        raise HTTPException (status_code=404 , detail="No file found")
        

@app.put('/contents/{id}')
async def edit_content(id:int,file:SingleFile,session:Annotated[Session,Depends(get_session)]):
    # existingfile = session.exec(select(SingleFile).where(SingleFile.id==id)).first()
    existingfile = session.get(SingleFile,id)
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
async def delete_content(id:int , session:Annotated[Session,Depends(get_session)] ):
    # file = session.exec(select(SingleFile).where(SingleFile.id==id)).first()
    file = session.get(SingleFile,id)
    if file:
        session.delete(file)
        session.commit()
        return {"Message : file deleted successfully"}
    else:
        raise HTTPException (status_code=404 , detail="No content found")
