from fastapi import APIRouter
from schemas.company_schema import enterCompany
from authentication.auth import get_current_user
from fastapi import Depends
from fastapi import HTTPException
from services.companies_service import showCompanies as sc,deleteCompany as dc,update_company as uc,saveCompany as SC

router = APIRouter()

@router.post("/company/")
def add_company(addCompany : enterCompany,user_id = Depends(get_current_user)):
    save_company=SC(addCompany, user_id)
    if not save_company:
        raise HTTPException(status_code=500, detail="company Not Saved")
    return {"message": "Company Saved successfully",
            "newCompanyId":save_company}
        
    

@router.get("/showcompanies/")
def showCompanies(user_id = Depends(get_current_user)):
    companies=sc(user_id)
    return companies
    
  

@router.put("/updateCompany/{companyId}/")
def updateApp(companyId :int,companyName:str,companySite:str,companyLocation:str):
    update_company=uc(companyName, companyLocation, companySite, companyId)
    if not update_company:
        raise HTTPException(status_code=404, detail="Company Not Updated")
    return {"message": "Company Updated successfully"}
    

@router.delete("/deleteCompany/{companyId}/")
def deleteCompany(companyId :int,user_id = Depends(get_current_user)):
    is_deleted=dc(companyId,user_id)
    if not is_deleted:
        raise HTTPException(status_code=404, detail="Company Not Found")
    return {"message": "company deleted successfully"}
    