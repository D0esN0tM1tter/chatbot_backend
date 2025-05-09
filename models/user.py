from sqlalchemy import Column, Integer, String 
from app.database.database import  SessionLocal
from app.database.base import Base


class User(Base) : 

    __tablename__="users" 

    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String, index=True) 
    email = Column(String , index=True)

    def __init__(self, id : int ,name : str , email : str) : 
        self.id = id 
        self.name = name 
        self.email = email
