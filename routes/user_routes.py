from fastapi import APIRouter
from schemas.user_schema import CreateUser,LoginRequest
from services.user_service import save_user as su,login as l
from fastapi import HTTPException




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
        
    