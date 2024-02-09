from school import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
class User (Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True, nullable= False)
    fname = Column(String(20), nullable= False)
    lname = Column(String(20), nullable= False)
    password = Column(String(50), nullable= False)
    creted = Column(DateTime, default=datetime.utcnow)