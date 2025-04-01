from pydantic import BaseModel, ValidationError, Field
from dataclasses import dataclass

class NormalUser:
    def __init__(self, id: int, name: str, age: int):
        self.id = id
        self.name = name
        self.age = age

    def __repr__(self):
        return f"NormalUser(id={self.id}, name={self.name}, age={self.age})"

@dataclass
class DataUser:
    id: int
    name: str
    age: int

class User(BaseModel):
    id: int
    name: str
    age: int = Field(gt=0, lt=120)  
    email: str = Field(regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$") 

try:
    user_data = {
        "id": 1,
        "name": "John Doe",
        "age": 25,
        "email": "john.doe@example.com"
    }
    user = User(**user_data)
    print("User created successfully:", user)

    invalid_user_data = {
        "id": "not_an_integer",  
        "name": "Jane Doe",
        "age": -5,              
        "email": "invalid_email" 
    }
    invalid_user = User(**invalid_user_data)
except ValidationError as e:
    print("Validation error:", e)

# print("User as dict:", user.model_dump())
# print("User as JSON:", user.model_dump_json())
