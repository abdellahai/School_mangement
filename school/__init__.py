from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///db')
LocalSession = sessionmaker(engine)
Base = declarative_base()
from school.models import User
Base.metadata.create_all(engine)
def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()
app = FastAPI()
from school import urls