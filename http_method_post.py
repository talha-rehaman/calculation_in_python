from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name:str
    age:int
    email:str
    bio: Optional[str]=None
    grade : str = "A"
u = User(name="Ali", age=20, email="ali@gmail.com",bio="I am a student")
print(u)
