from school import app, get_db
from fastapi import Depends
from school.schema import SchemaUser
from school.models import User
from sqlalchemy.orm import Session
@app.get('/')
def home():
    return{'message':'home'}

@app.post('/user')
def addUser(user:SchemaUser, db:Session = Depends(get_db)):
    user_db = User(email = user.email, fname = user.fname, lname = user.lname, password = user.password)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db


@app.get('/user')
def getUsers(db:Session=Depends(get_db)):
    users = db.query(User).all()
    return {'users':users}