from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# specifying the database url 
DATABASE_URL="sqlite:///./database"

# creating the engine ( bridge between the application and the databse) 
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread" : False}) 

# intanciating a session factory ( handling transaction ) 
SessionLocal = sessionmaker(bind=engine , autoflush=False, autocommit= False)

# this will method will be used to ensure dependency injection in the repository class
def get_db()  : 
    session = SessionLocal()

    try :
        yield session 
    finally :
        session.close()