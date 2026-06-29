from jose import jwt
from datetime import datetime, timedelta,timezone
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from fastapi import HTTPException


SECRET_KEY = "03349854664"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30



def create_access_token(user_id: str):

    payload = {
     "sub": str(user_id),

    "exp": datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    token=jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)
    return(token)

security_scheme = OAuth2PasswordBearer(tokenUrl="/loggingIn")

def get_current_user(token = (Depends(security_scheme))):
   try:
    payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    print(payload)
    user_id = payload["sub"]
    return (int(user_id))
   except Exception as e:
    print(e)
    raise HTTPException(
        status_code=401,
        detail="Invalid or expired token"
    )
       

    
    

    
