from typing import Any, List, Optional
import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from reqherd.webservice import crud, models, schemas
from reqherd.webservice.api import dependencies as deps


logger = logging.getLogger(__name__)


router = APIRouter()


@router.get("/", response_model=List[schemas.SystemRequirement])
def get_system_requirements(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve system requirements.
    """
    system_requirements = crud.sysreq.get_multi(db, skip=skip, limit=limit)
    logger.debug(system_requirements)
    return system_requirements


@router.post("/", response_model=List[schemas.SystemRequirement])
def create_system_requirements(
    *,
    db: Session = Depends(deps.get_db),
    system_requirements_in: List[schemas.SystemRequirementCreate],
) -> Any:
    """
    Create new system requirements.
    """
    system_requirements = list()
    for system_requirement_in in system_requirements_in:
        system_requirement = crud.sysreq.create(db=db, obj_in=system_requirement_in)
        system_requirements.append(system_requirement)
    logger.debug(system_requirements)
    return system_requirements


@router.put("/{id}", response_model=schemas.SystemRequirement)
def update_system_requirement(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    system_requirement_in: schemas.SystemRequirementUpdate,
) -> Any:
    """
    Update system requirement.
    """
    systemrequirement = crud.sysreq.get(db=db, id=id)
    if not systemrequirement:
        raise HTTPException(status_code=404, detail="Record not found")
    systemrequirement = crud.sysreq.update(
        db=db, db_obj=systemrequirement, obj_in=system_requirement_in
    )
    logger.debug(systemrequirement)
    return systemrequirement


@router.get("/{id}", response_model=schemas.SystemRequirement)
def get_system_requirement(*, db: Session = Depends(deps.get_db), id: int) -> Any:
    """
    Get system requirement by ID.
    """
    systemrequirement = crud.sysreq.get(db=db, id=id)
    if not systemrequirement:
        raise HTTPException(status_code=404, detail="Record not found")
    logger.debug(systemrequirement)
    return systemrequirement


@router.delete("/{id}", response_model=schemas.SystemRequirement)
def delete_system_requirement(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete a system requirement.
    """
    systemrequirement = crud.sysreq.get(db=db, id=id)
    if not systemrequirement:
        raise HTTPException(status_code=404, detail="Record not found")
    systemrequirement = crud.sysreq.remove(db=db, id=id)
    logger.debug(systemrequirement)
    return systemrequirement
