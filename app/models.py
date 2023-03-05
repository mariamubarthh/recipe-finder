from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from .database import Base
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship


#recipe model to create recipes table
class Recepie(Base):
    __tablename__= "Recepies"
    
   
    dishname= Column(String,primary_key=True, nullable=False)
    instructions= Column(String, nullable=False)
    ingredients= Column(String, nullable=False)
    image_path = Column(String,nullable=False)
    
    
#user model to create users table
class User(Base):
    __tablename__="users"
    
    id= Column(Integer, primary_key=True, nullable=False)
    email=Column(String, nullable=False, unique=True)
    password=Column(String,nullable=False)
    role = Column(String,nullable=False)


    
    
    