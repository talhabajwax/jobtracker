from schemas.company_schema import enterCompany
from repositeries.companies_repo import save_company as sc,delete_company as dc,update_company as uc,show_company as SC


def saveCompany(company:enterCompany):
    isSaved=sc(company.companyName,company.websiteName,company.locationName)
    if isSaved ==  None:
        return False
    return isSaved

def deleteCompany(company_id,user_id):
    isDeleted=dc(company_id,user_id)
    if isDeleted ==  0:
        return False
    return isDeleted

def update_company(companyName,companyLocation,companySite,companyId):
    isUpdated=uc(companyName,companyLocation,companySite,companyId)
    if isUpdated == 0:
        return False
    return isUpdated

def showCompanies(user_id):
    companies=SC(user_id)
    return companies