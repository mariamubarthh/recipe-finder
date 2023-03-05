from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from psycopg2.extras import RealDictCursor
from .config import settings

#connection string
SQLALCHEMY_CONN_URL=f'postgresql://{settings.database_username}:{settings.database_pw}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

#engine responsible for sql alchemy to connect to db
engine=create_engine(SQLALCHEMY_CONN_URL)

SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()                      #session func used for talking to databases
    try:                                     #we will call this func everytime we get a req to our api endpoints
        yield db 
    finally:
        db.close()
        
        
