from pydantic import BaseModel,fields,StringConstraints
from typing import Annotated

CleanText = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]

class enterCompany(BaseModel):
    companyName : CleanText
    websiteName : CleanText
    locationName : str | None