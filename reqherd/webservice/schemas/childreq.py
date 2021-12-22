from typing import Optional
from datetime import datetime

from .base import BaseRequirementSchema

# Shared properties
class ChildRequirementBase(BaseRequirementSchema):
    doc_prefix: Optional[str] = "SRS"
    system_requirement_id: Optional[int]


# Properties to receive on item creation
class ChildRequirementCreate(ChildRequirementBase):
    pass


# Properties to receive on item update
class ChildRequirementUpdate(ChildRequirementBase):
    pass


# Properties shared by models stored in DB
class ChildRequirementInDBBase(ChildRequirementBase):
    id: int
    doc_prefix: str
    definition: str
    modified_date: datetime
    system_requirement_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class ChildRequirement(ChildRequirementInDBBase):
    pass


# Properties properties stored in DB
class ChildRequirementInDB(ChildRequirementInDBBase):
    pass
