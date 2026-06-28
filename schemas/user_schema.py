
from pydantic import BaseModel,StringConstraints,EmailStr
from typing import Annotated

CleanText = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=10)]

class CreateUser(BaseModel):
    email: EmailStr
    password: CleanText
    
class login(BaseModel):
    email  : EmailStr
    password : CleanText
    
