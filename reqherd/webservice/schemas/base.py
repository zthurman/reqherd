from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class BaseRequirementSchema(BaseModel):
    doc_prefix: Optional[str] = None
    definition: Optional[str] = None
    modified_date: Optional[datetime] = None
