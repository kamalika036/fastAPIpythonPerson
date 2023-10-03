from fastapi import FastAPI
import person
from db import engine 
from db import SessionLocal 
#import crud to give access to the operations that we defined 
import crud 
from fastapi import FastAPI 
from sqlalchemy.orm import Session
from fastapi import Depends 



app=FastAPI()

@app.get("/")
def home():
    return {"name":"Kamalika","address":"Kolkata", "pin":711201}

def get_db(): 
    db = SessionLocal() 
    try: 
        yield db 
    finally: 
        db.close()

#create the database tables on app startup or reload 
person.Base.metadata.create_all(bind=engine)

print("database is created")


#define endpoint 
@app.post("/create_person") 
def create_person(name:str, address:str, age:int, db:Session = Depends(get_db)): 
    person = crud.create_person(db=db, name=name, address=address, age=age) 
##return object created 
    return {"newly created person": person}


@app.get("/list_person") 
def list_person(db:Session = Depends(get_db)): 
    """ 
    Fetch a list of all person object 
    Returns a list of objects 
    """ 
    person_list = crud.list_person(db=db) 
    return person_list 


@app.put("/update_person/{id}/") #id is a path parameter 
def update_friend(id:int, name:str, address:str, age:int, db:Session=Depends(get_db)): 
    #get friend object from database 
    db_person = crud.get_person(db=db, id=id) 
    #check if friend object exists 
    if db_person: 
        updated_person = crud.update_person(db=db, id=id, name=name, address=address, age=age) 
        return updated_person
    else: 
        return {"error": f"Friend with id {id} does not exist"} 

#get/retrieve friend  
@app.get("/get_person/{id}/") #id is a path parameter 
def get_person(id:int, db:Session = Depends(get_db)): 
    """ 
    the path parameter for id should have the same name as the argument for id 
    so that FastAPI will know that they refer to the same variable 
Returns a friend object if one with the given id exists, else null 
    """ 
    person = crud.get_person(db=db, id=id) 
    return person  


#get/retrieve friend by name 
@app.get("/getbyname_person/{name}/") #id is a path parameter 
def getbyname_person(name:str, db:Session = Depends(get_db)): 
    """ 
    the path parameter for id should have the same name as the argument for id 
    so that FastAPI will know that they refer to the same variable 
Returns a friend object if one with the given id exists, else null 
    """ 
    person = crud.getbyname_person(db=db, name=name) 
    return person 


#get/retrieve friend by address 
@app.get("/getbyaddress_person/{address}/") #id is a path parameter 
def getbyaddress_person(address:str, db:Session = Depends(get_db)): 
    """ 
    the path parameter for id should have the same name as the argument for id 
    so that FastAPI will know that they refer to the same variable 
Returns a friend object if one with the given id exists, else null 
    """ 
    person = crud.getbyaddress_person(db=db, address=address) 
    return person 


@app.delete("/delete_person/{id}/") #id is a path parameter 
def delete_person(id:int, db:Session=Depends(get_db)): 
    #get person object from database 
    db_person = crud.get_person(db=db, id=id) 
    #check if friend object exists 
    if db_person: 
        return crud.delete_person(db=db, id=id) 
    else: 
        return {"error": f"person with id {id} does not exist"}
    


