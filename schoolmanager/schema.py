from pydantic import BaseModel


class SchemaUser(BaseModel):
    email: str
    password: str