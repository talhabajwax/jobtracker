from fastapi import APIRouter
from schemas.application_schema import Enterapplication

router = APIRouter()

@router.post("/application/")
def enterApp (application : Enterapplication):
    return{'message':"Application Saved"}
