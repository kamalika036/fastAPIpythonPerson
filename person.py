from sqlalchemy import Column, Integer, String 
 
from db import Base 
 
# model/table 
class  Person(Base): 
    __tablename__ = "person" 
 
    # fields  
    id = Column(Integer,primary_key=True, index=True) 
    name = Column(String(30)) 
    address = Column(String(30)) 
    age = Column(Integer)