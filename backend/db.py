from sqlmodel import SQLModel, Session, create_engine
from backend import setting


connection_string : str = str(setting.DATABASE_URL).replace("postgresql","postgresql+psycopg")

# engine is one for whole application
engine = create_engine(connection_string,connect_args={"sslmode":"require"},pool_recycle=300,pool_size=10,echo=True)

def create_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        # yield is generator function
        yield session
