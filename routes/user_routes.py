from fastapi import APIRouter
from schemas.user_schema import CreateUser

router = APIRouter()

@router.post("/users/")
def create_user(user: CreateUser):
    # Logic to create a user in the database
    return {"message": "User created successfully", "user": user}
    