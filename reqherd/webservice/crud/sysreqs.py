from typing import List
import logging

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from reqherd.webservice.crud.base import CRUDBase
from reqherd.webservice.models.sysreq import System_Requirement
from reqherd.webservice.schemas.sysreq import (
    SystemRequirementCreate,
    SystemRequirementUpdate,
)


logger = logging.getLogger(__name__)


class CRUDSystemRequirement(
    CRUDBase[System_Requirement, SystemRequirementCreate, SystemRequirementUpdate]
):
    def create(
        self, db: Session, *, obj_in: SystemRequirementCreate
    ) -> System_Requirement:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        try:
            db.commit()
        except Exception as exc:
            raise HTTPException(
                status_code=422,
                detail=f"{exc}",
            ) from exc
        db.refresh(db_obj)
        return db_obj

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[System_Requirement]:
        query = (
            db.query(self.model).order_by(self.model.id.asc()).offset(skip).limit(limit)
        )
        logger.debug(query.statement.compile(compile_kwargs={"literal_binds": True}))
        return query.all()


sysreq = CRUDSystemRequirement(System_Requirement)
