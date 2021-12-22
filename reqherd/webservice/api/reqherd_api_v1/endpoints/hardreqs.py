from typing import Any, List, Optional
import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from reqherd.webservice import crud, models, schemas
from reqherd.webservice.api import dependencies as deps


logger = logging.getLogger(__name__)


router = APIRouter()


@router.get("/", response_model=List[schemas.ChildRequirement])
def get_hardware_requirements(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve software requirements.
    """
    hardware_requirements = crud.hardreq.get_multi(db, skip=skip, limit=limit)
    logger.debug(hardware_requirements)
    return hardware_requirements


@router.post("/", response_model=List[schemas.ChildRequirement])
def create_hardware_requirements(
    *,
    db: Session = Depends(deps.get_db),
    hardware_requirements_in: List[schemas.ChildRequirementCreate],
) -> Any:
    """
    Create new software requirements.
    """
    hardware_requirements = list()
    for hardware_requirement_in in hardware_requirements_in:
        hardware_requirement = crud.hardreq.create(
            db=db, obj_in=hardware_requirement_in
        )
        hardware_requirements.append(hardware_requirement)
    logger.debug(hardware_requirements)
    return hardware_requirements


@router.put("/{id}", response_model=schemas.ChildRequirement)
def update_hardware_requirement(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    hardware_requirement_in: schemas.ChildRequirementUpdate,
) -> Any:
    """
    Update software requirement.
    """
    SoftwareRequirement = crud.hardreq.get(db=db, id=id)
    if not SoftwareRequirement:
        raise HTTPException(status_code=404, detail="Record not found")
    SoftwareRequirement = crud.hardreq.update(
        db=db, db_obj=SoftwareRequirement, obj_in=hardware_requirement_in
    )
    logger.debug(SoftwareRequirement)
    return SoftwareRequirement


@router.get("/{id}", response_model=schemas.ChildRequirement)
def get_hardware_requirement(*, db: Session = Depends(deps.get_db), id: int) -> Any:
    """
    Get software requirement by ID.
    """
    SoftwareRequirement = crud.hardreq.get(db=db, id=id)
    if not SoftwareRequirement:
        raise HTTPException(status_code=404, detail="Record not found")
    logger.debug(SoftwareRequirement)
    return SoftwareRequirement


@router.delete("/{id}", response_model=schemas.ChildRequirement)
def delete_hardware_requirement(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete a software requirement.
    """
    SoftwareRequirement = crud.hardreq.get(db=db, id=id)
    if not SoftwareRequirement:
        raise HTTPException(status_code=404, detail="Record not found")
    SoftwareRequirement = crud.hardreq.remove(db=db, id=id)
    logger.debug(SoftwareRequirement)
    return SoftwareRequirement
