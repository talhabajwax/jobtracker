from repositeries.application_repo import delete_application as da,save_application as sa,show_applications as SA,update_application_status as ups
from repositeries.application_repo import get_application as ga

def delete_application(app_id:int,user_id:int):
    rowCount=da(app_id,user_id)
    if rowCount == 0:
        return False
    else:
        return True

def save_application(user_id,company_id,status_id,jobtitle,appliedAt,jobUrl):
    new_id=sa(user_id,company_id,status_id,jobtitle,appliedAt,jobUrl)
    if new_id ==  None:
        return False
    return new_id
    
def show_applications(user_id):
    application=SA(user_id)
    return application


def update_application_status(application_id, new_status_id,user_id):
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