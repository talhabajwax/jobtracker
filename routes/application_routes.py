from fastapi import APIRouter
from schemas.application_schema import Enterapplication
from database import save_application

router = APIRouter()

@router.post("/application/")
def enterApp (application : Enterapplication):
    save_application(application.user_id,application.company_id,application.status_id,application.role_title,application.applied_date,application.job_url)
    return{'message':"Application Saved"}
