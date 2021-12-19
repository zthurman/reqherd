from typing import Optional
from datetime import datetime

from ..schemas.base import BaseRequirementSchema

# Shared properties
class SystemRequirementBase(BaseRequirementSchema):
    pass


# Properties to receive on item creation
class SystemRequirementCreate(SystemRequirementBase):
    pass


# Properties to receive on item update
class SystemRequirementUpdate(SystemRequirementBase):
    pass


# Properties shared by models stored in DB
class SystemRequirementInDBBase(SystemRequirementBase):
    id: int
    doc_prefix: str
    definition: str
    modified_date: datetime

    class Config:
        orm_mode = True


# Properties to return to client
class SystemRequirement(SystemRequirementInDBBase):
    pass


# Properties properties stored in DB
class SystemRequirementInDB(SystemRequirementInDBBase):
    pass
