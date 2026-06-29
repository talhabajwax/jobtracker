from fastapi import APIRouter
from schemas.company_schema import enterCompany
from database import save_company,show_company,delete_company,update_company
from authentication.auth import get_current_user
from fastapi import Depends

router = APIRouter()

@router.post("/company/")
def add_company(addCompany : enterCompany):
    save_company(addCompany.companyName,addCompany.websiteName,addCompany.locationName)
    return {'message':'Company successfully added'}

@router.get("/showcompanies/")
def showCompanies(user_id = Depends(get_current_user)):
  
    return{"companies":show_company()}

@router.put("/updateCompany/{companyId}/")
def updateApp(companyId :int,companyName:str,companySite:str,companyLocation:str):
    update_company(companyName, companyLocation, companySite, companyId)
    return{"message":"updated"}

@router.delete("/deleteCompany/{companyId}/")
def deleteApp(companyId :int):
    delete_company(companyId)
    return{"message":"deleted"}