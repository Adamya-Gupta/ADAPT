from fastapi import FastAPI
from sqlmodel import SQLModel , Field, create_engine ,Session
from backend import setting


class adapt (SQLModel,table = True):
    id : int | None = Field(default = None,primary_key = True)
    content : str = Field(index = True)
    doc_type : str | None = Field(default=None,index = True)

connection_string : str = str(setting.DATABASE_URL).replace("postgresql","postgresql+psycopg")

# engine is one for whole application
engine = create_engine(connection_string,connect_args={"sslmode":"require"},pool_recycle=300,pool_size=10,echo=True)

SQLModel.metadata.create_all(engine)

doc1  = adapt(content="first content" ,doc_type = "docs")
doc2  = adapt(content="second task" , doc_type = "pdf")

# session : separate session for each functionality/transaction
session = Session(engine)

#create docs in database

session.add(doc1)
session.add(doc2)
print(f'Before Commit {doc1}')
session.commit()
session.refresh(doc1)
print(f'After Commit {doc2}')
session.close()


app :FastAPI = FastAPI()

@app.get('/')
async def root():
    return {"message" : "Welcome to the fastapi server"}

@app.post('/contents/')
async def create_content():
    ...

@app.get('/contents/')
async def get_all():
    ...

@app.get('/contents/{id}')
async def get_single_content():
    ...

@app.put('/contents/{id}')
async def edit_content():
    ...

app.delete('/contents/{id}')
async def delete_content():
    ...