from fastapi import APIRouter
from schemas.application_schema import Enterapplication
from database import save_application, show_applications,update_application_status,delete_application

router = APIRouter()

@router.post("/application/")
def enterApp (application : Enterapplication):
    save_application(application.user_id,application.company_id,application.status_id,application.role_title,application.applied_date,application.job_url)
    return{'message':"Application Saved"}

@router.get("/showApplications")
def showApps():
    return{'applications': show_applications()}

@router.put("/updateApplication")
def updateApplication(appId :int,newStatus :int):
    update_application_status(appId,newStatus)
    return{"message":"updated"}

@router.delete("/deleteApplication/{appId}")
def deleteApp(appId :int):
    delete_application(appId)
    return{'message':'application Deleted'}
