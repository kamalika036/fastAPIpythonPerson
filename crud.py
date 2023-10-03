from sqlalchemy.orm import Session 
 
""" 
Session manages persistence operations for ORM-mapped objects. 
Let's just refer to it as a database session for simplicity 
""" 
 
from person import Person
 
 
def create_person(db:Session, name, address, age): 
    """ 
    function to create a friend model object 
    """ 
    # create friend instance  
    new_person = Person(name=name, address=address, age=age) 
    #place object in the database session 
    db.add(new_person) 
    #commit your instance to the database 
    db.commit() 
    #reefresh the attributes of the given instance 
    db.refresh(new_person) 
    return new_person

 
def list_person(db:Session): 
    """ 
    Return a list of all existing Person records 
    """ 
    all_person = db.query(Person).all() 
    return all_person 
 
 

def get_person(db:Session, id:int): 
    """ 
    get the first record with a given id, if no such record exists, will return null 
    """ 
    db_person = db.query(Person).filter(Person.id==id).first() 
    return db_person

 
def getbyname_person(db:Session, name:str): 
    """ 
    get the first record with a given id, if no such record exists, will return null 
    """ 
    db_person = db.query(Person).filter(Person.name==name).first() 
    return db_person 


def getbyaddress_person(db:Session, address:str): 
    """ 
    get the first record with a given id, if no such record exists, will return null 
    """ 
    db_person = db.query(Person).filter(Person.address==address).first() 
    return db_person 


def update_person(db:Session, id:int, name: str, address: str, age:int): 
    """ 
    Update a Person object's attributes 
    """ 
    db_person= get_person(db=db, id=id) 
    db_person.name = name 
    db_person.address = address
    db_person.age = age 
 
    db.commit() 
    db.refresh(db_person) #refresh the attribute of the given instance 
    return db_person
 
def delete_person(db:Session, id:int): 
    """ 
    Delete a person object 
    """ 
    db_person = get_person(db=db, id=id) 
    db.delete(db_person) 
    db.commit() #save changes to db



