from fastapi import APIRouter
from schemas.user_schema import CreateUser,LoginRequest
from passlib.context import CryptContext
from database import save_user,login_user
from authentication.auth import create_access_token
from services.user_service import save_user as su,login as l
from fastapi import HTTPException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


router = APIRouter()



@router.post("/users/")
def create_user(user: CreateUser):
    new_user=su(user)
    if new_user == False:
                raise HTTPException(status_code=409, detail="user Not Saved")
    return {"message": "user Saved successfully",
            "newUserId":new_user}
    

@router.post("/loggingIn")
def loggingIn(user:LoginRequest):
    response=l(user)
    if not response :
        raise HTTPException(status_code=401, detail="Invalid mail or password")
    return (response)
        
    