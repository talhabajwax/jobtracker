from repositeries.user_repo import save_user as sa ,login_user as lu,existing_user as eu
from passlib.context import CryptContext
from authentication.auth import create_access_token
from schemas.user_schema import CreateUser,LoginRequest

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def save_user(saveUser: CreateUser):
    existingEmail=eu(saveUser.email)
    if existingEmail == None:
        password_hash = pwd_context.hash(saveUser.password)
        new_user=sa(saveUser.email,password_hash)
        return new_user
    return False
        
def login(user: LoginRequest):
        response = lu(user.email)
        if response is None :
         return False
        check=pwd_context.verify(user.password,response[1])
        if check is True:
         token = create_access_token(response[0])
         return{
              "access_token": token,
              "token_type": "bearer"
        }
        return False

        

    