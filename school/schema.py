from pydantic import BaseModel

class SchemaUser(BaseModel):
    email : str
    fname: str
    lname: str
    password : str