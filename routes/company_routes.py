from fastapi import APIRouter
from schemas.company_schema import enterCompany
from database import save_company

router = APIRouter()

@router.post("/company/")
def add_company(addCompany : enterCompany):
    save_company(addCompany.companyName,addCompany.websiteName,addCompany.locationName)
    return {'message':'Company successfully added'}