from fastapi import FastAPI , Depends , HTTPException
from sqlmodel import SQLModel , Field, create_engine ,Session ,select
from backend import setting
from typing import Annotated
from contextlib import asynccontextmanager


class adapt (SQLModel,table = True):
    id : int | None = Field(default = None,primary_key = True)
    content : str = Field(index = True)
    doc_type : str | None = Field(default=None,index = True)

connection_string : str = str(setting.DATABASE_URL).replace("postgresql","postgresql+psycopg")

# engine is one for whole application
engine = create_engine(connection_string,connect_args={"sslmode":"require"},pool_recycle=300,pool_size=10,echo=True)

def create_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        # yield is generator function
        yield session

# First task after starting of the app should be to create tables
@asynccontextmanager
async def lifespan(app:FastAPI):
    print('Creating Tables')
    create_tables()
    print('Tables Created')
    yield

app :FastAPI = FastAPI(lifespan=lifespan,title="ADAPT",version='1.0.0')

@app.get('/')
async def root():
    return {"message" : "Welcome to the fastapi server"}


# injected session dependency 
@app.post('/contents/',response_model=adapt)
async def create_content(file : adapt , session:Annotated[Session,Depends(get_session)]):
    session.add(file)
    session.commit()
    session.refresh(file)
    return file

@app.get('/contents/',response_model= list[adapt])
async def get_all(session:Annotated[Session,Depends(get_session)]):
    statement = select(adapt)
    allfiles = session.exec(statement).all()
    if allfiles: 
        return allfiles
    else:
        raise HTTPException (status_code=404 , detail="No files found")


@app.get('/contents/{id}',response_model=adapt)
async def get_single_content(id: int, session:Annotated[Session,Depends(get_session)]):
    singlefile = session.exec(select(adapt).where(adapt.id == id)).first()
    if singlefile:
        return singlefile
    else:
        raise HTTPException (status_code=404 , detail="No file found")
        

@app.put('/contents/{id}')
async def edit_content(id:int,file:adapt,session:Annotated[Session,Depends(get_session)]):
    # existingfile = session.exec(select(adapt).where(adapt.id==id)).first()
    existingfile = session.get(adapt,id)
    if existingfile:
        existingfile = file.content

        existingfile.is_completed = file.is_completed
        existingfile.doc_type = file.doc_type

        session.add(existingfile)
        session.commit()
        session.refresh(existingfile)
        return existingfile
    else:
        raise HTTPException (status_code=404 , detail="No content found")

@app.delete('/contents/{id}')
async def delete_content(id:int , session:Annotated[Session,Depends(get_session)] ):
    # file = session.exec(select(adapt).where(adapt.id==id)).first()
    file = session.get(adapt,id)
    if file:
        session.delete(file)
        session.commit()
        return {"Message : file deleted successfully"}
    else:
        raise HTTPException (status_code=404 , detail="No content found")
