from pydantic import BaseModel

class Enterapplication(BaseModel):
    user_id : int
    company_id  : int
    status_id  : int
    role_title : str
    applied_date : str
    job_url : str