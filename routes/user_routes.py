from fastapi import APIRouter
from schemas.user_schema import CreateUser
from passlib.context import CryptContext
from database import save_user

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


router = APIRouter()



@router.post("/users/")
def create_user(user: CreateUser):
    # Logic to create a user in the database
    password_hash = pwd_context.hash(user.password)
    response=save_user(user.email,password_hash)
    
   
    return {"message" : response}
    