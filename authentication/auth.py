from jose import jwt
from datetime import datetime, timedelta,timezone


SECRET_KEY = "03349854664"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30



def create_access_token(user_id: int):

    payload = {
     "sub": user_id,

    "exp": datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    token=jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)
    return(token)

# def decode_jwt(token):
#     payload = {
#      "sub": user_id,

#     "exp": datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     }
        
#     decoded_token=jwt.decode(payload,SECRET_KEY,algorithm=ALGORITHM)
#     return(decoded_token)
 
