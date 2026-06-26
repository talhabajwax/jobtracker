from pydantic import BaseModel
from datetime import date

class Enterapplication(BaseModel):
    user_id : int
    company_id  : int
    status_id  : int
    role_title : str
    applied_date : date
    job_url : str