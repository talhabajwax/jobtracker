from schemas.company_schema import enterCompany
from repositeries.companies_repo import save_company as sc,delete_company as dc, show_company_by_id,update_company as uc,show_company as SC


def saveCompany(company:enterCompany,user_id):
    isSaved=sc(company.companyName,company.websiteName,company.locationName, user_id)
    if isSaved ==  None:
        return False
    return isSaved

def deleteCompany(company_id,user_id):
    isDeleted=dc(company_id,user_id)
    if isDeleted ==  0:
        return False
    return isDeleted

def update_company(companyName,companyLocation,companySite,companyId,user_id):
    isUpdated=uc(companyName,companyLocation,companySite,companyId,user_id)
    if isUpdated == 0:
        return False
    return isUpdated

def showCompanies(user_id):
    companies=SC(user_id)
    return companies

def showCompany(company_Id, user_id):
    company=show_company_by_id(company_Id, user_id)
    if company is None:
        return False
    else:
        return company