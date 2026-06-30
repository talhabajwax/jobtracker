from fastapi import APIRouter
from schemas.application_schema import Enterapplication
from database import save_application, show_applications,update_application_status,delete_application
from authentication.auth import get_current_user
from fastapi import Depends

router = APIRouter()

@router.post("/application/")
def enterApp (application : Enterapplication,user_id = Depends(get_current_user)):
    save_application(user_id ,application.company_id,application.status_id,application.role_title,application.applied_date,application.job_url)
    return{'message':"Application Saved"}

@router.get("/showApplications")
def showApps(user_id = Depends(get_current_user)):
    return {"applications": show_applications(user_id)}


@router.put("/updateApplication")
def updateApplication(appId :int,newStatus :int,user_id = Depends(get_current_user)):
    update_application_status(appId,newStatus,user_id)
    return{"message":"updated"}

@router.delete("/deleteApplication/{appId}")
def deleteApp(appId :int,user_id = Depends(get_current_user)):
    delete_application(appId,user_id)
    return{'message':'application Deleted'}
