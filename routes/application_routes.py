from fastapi import APIRouter
from schemas.application_schema import Enterapplication
from authentication.auth import get_current_user
from fastapi import Depends
from services.application_service import delete_application as da,save_application as sa,show_applications as SA,update_application_status as ups
from fastapi import HTTPException

router = APIRouter()

@router.post("/application/")
def save_application (application : Enterapplication,user_id = Depends(get_current_user)):
    new_id=sa(user_id ,application.company_id,application.status_id,application.role_title,application.applied_date,application.job_url)
    if not new_id:
        raise HTTPException(status_code=500, detail="Application Not Saved")
    return {"message": "Application Saved successfully",
            "newAppId":new_id}


@router.get("/showApplications")
def show_applications(user_id = Depends(get_current_user)):
    applications=SA(user_id)
    return applications


@router.put("/updateApplication")
def update_application_status(application_id :int,new_status_id :int,user_id = Depends(get_current_user)):
    is_updated=ups(application_id, new_status_id,user_id)
    if not is_updated:
        raise HTTPException(status_code=404, detail="Application Not Updated")
    return {"message": "Application Updated successfully"}


@router.delete("/deleteApplication/{appId}")
def delete_application(appId :int,user_id = Depends(get_current_user)):
    is_deleted=da(appId,user_id)
    if not is_deleted:
        raise HTTPException(status_code=404, detail="Application Not Found")
    return {"message": "Application deleted successfully"}
