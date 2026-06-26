from fastapi import APIRouter
from schemas.application_schema import Enterapplication
from database import save_application, show_applications

router = APIRouter()

@router.post("/application/")
def enterApp (application : Enterapplication):
    save_application(application.user_id,application.company_id,application.status_id,application.role_title,application.applied_date,application.job_url)
    return{'message':"Application Saved"}

@router.get("/showApplications")
def showApps():
    return{'applications': show_applications()}
