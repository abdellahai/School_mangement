from schoolmanager import Base
from sqlalchemy import  Column, Integer, String, DateTime
from datetime import datetime

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    email = Column (String(50), nullable = False, unique = True)
    password = Column(String(50), nullable = False)
    create_date = Column(DateTime, default = datetime.utcnow)
