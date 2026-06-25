from fastapi import APIRouter
from schemas.company_schema import enterCompany

router = APIRouter()

@router.post("/company/")
def add_company(addCompany : enterCompany):
    return {'message':'Company successfully added'}