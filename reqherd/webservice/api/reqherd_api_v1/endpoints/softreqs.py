from typing import Any, List, Optional
import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from reqherd.webservice import crud, models, schemas
from reqherd.webservice.api import dependencies as deps


logger = logging.getLogger(__name__)


router = APIRouter()


@router.get("/", response_model=List[schemas.ChildRequirement])
def get_software_requirements(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve software requirements.
    """
    software_requirements = crud.softreq.get_multi(db, skip=skip, limit=limit)
    logger.debug(software_requirements)
    return software_requirements


@router.post("/", response_model=List[schemas.ChildRequirement])
def create_software_requirements(
    *,
    db: Session = Depends(deps.get_db),
    software_requirements_in: List[schemas.ChildRequirementCreate],
) -> Any:
    """
    Create new software requirements.
    """
    software_requirements = list()
    for software_requirement_in in software_requirements_in:
        software_requirement = crud.softreq.create(
            db=db, obj_in=software_requirement_in
        )
        software_requirements.append(software_requirement)
    logger.debug(software_requirements)
    return software_requirements


@router.put("/{id}", response_model=schemas.ChildRequirement)
def update_software_requirement(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    software_requirement_in: schemas.ChildRequirementUpdate,
) -> Any:
    """
    Update software requirement.
    """
    SoftwareRequirement = crud.softreq.get(db=db, id=id)
    if not SoftwareRequirement:
        raise HTTPException(status_code=404, detail="Record not found")
    SoftwareRequirement = crud.softreq.update(
        db=db, db_obj=SoftwareRequirement, obj_in=software_requirement_in
    )
    logger.debug(SoftwareRequirement)
    return SoftwareRequirement


@router.get("/{id}", response_model=schemas.ChildRequirement)
def get_software_requirement(*, db: Session = Depends(deps.get_db), id: int) -> Any:
    """
    Get software requirement by ID.
    """
    SoftwareRequirement = crud.softreq.get(db=db, id=id)
    if not SoftwareRequirement:
        raise HTTPException(status_code=404, detail="Record not found")
    logger.debug(SoftwareRequirement)
    return SoftwareRequirement


@router.delete("/{id}", response_model=schemas.ChildRequirement)
def delete_software_requirement(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete a software requirement.
    """
    SoftwareRequirement = crud.softreq.get(db=db, id=id)
    if not SoftwareRequirement:
        raise HTTPException(status_code=404, detail="Record not found")
    SoftwareRequirement = crud.softreq.remove(db=db, id=id)
    logger.debug(SoftwareRequirement)
    return SoftwareRequirement
