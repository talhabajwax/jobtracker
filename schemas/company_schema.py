from pydantic import BaseModel

class enterCompany(BaseModel):
    companyName : str
    websiteName : str