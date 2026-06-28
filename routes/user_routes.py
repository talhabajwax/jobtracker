from fastapi import APIRouter
from schemas.user_schema import CreateUser,login
from passlib.context import CryptContext
from database import save_user,login
from authentication.auth import create_access_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


router = APIRouter()



@router.post("/users/")
def create_user(user: CreateUser):
    # Logic to create a user in the database
    password_hash = pwd_context.hash(user.password)
    response=save_user(user.email,password_hash)
    
   
    return {"message" : response}

@router.post("/login")
def loggingIn(user :login):
    response = login(user.email)
    if response is None :
        return ("Invalid email or password")
    check=pwd_context.verify(user.password,response[1])
    if check is True:
        token = create_access_token(response[0])
        return{
              "access_token": token,
              "token_type": "bearer"
        }
    if check is False:
        return("Invalid email or password")
        
    