from schoolmanager import app, creerSession
from schoolmanager.schema import SchemaUser
from sqlalchemy.orm import  Session #Importation de gestionaire de session et de donnee de type session
from schoolmanager.models import User
from fastapi import Depends


@app.get('/')
def home():
    return {'message':'Hello'}

@app.post('/user')
def add_user(schemauser : SchemaUser, db_session:Session = Depends(creerSession)):
    user = User(email = schemauser.email, password = schemauser.password)
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return {'user':user}