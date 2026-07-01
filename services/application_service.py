from repositeries.application_repo import delete_application as da,save_application as sa,show_applications as SA,update_application_status as ups
from repositeries.application_repo import get_application as ga,duplicate_application as da,validate_status_id as vs
from repositeries.companies_repo import validate_company_id as vc

def delete_application(app_id:int,user_id:int):
    rowCount=da(app_id,user_id)
    if rowCount == 0:
        return False
    else:
        return True

def save_application(user_id,company_id,status_id,jobtitle,appliedAt,jobUrl):

    validate_company=vc(company_id,user_id)
    if not validate_company:
        return "Invalid Company"
    validate_status=vs(status_id)
    if not validate_status:
        return "Invalid Status"
    duplicate=da(user_id,company_id,jobtitle)
    if duplicate:
        return 'Duplicate Application'
    new_id=sa(user_id,company_id,status_id,jobtitle,appliedAt,jobUrl)
    if new_id == None:
        return False
    return new_id






    
def show_applications(user_id):
    application=SA(user_id)
    return application


def update_application_status(application_id, new_status_id,user_id):
    validate_status=vs(new_status_id)
    if not validate_status:
        return "Invalid Status"
    
    updated_row=ups(application_id, new_status_id,user_id)
    if updated_row == 0:
        return False
    else:
        return True
    
def get_application(application_id, user_id):
    application=ga(application_id, user_id)
    if application is None:
        return False
    else:
        return application