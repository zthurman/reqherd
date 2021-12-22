from fastapi import APIRouter

from reqherd.webservice.config import REQHERD_API_V1_STR

from reqherd.webservice.api.reqherd_api_v1.endpoints import sysreqs, softreqs, hardreqs

reqherd_api_router = APIRouter()
reqherd_api_router.include_router(
    sysreqs.router,
    prefix=f"{REQHERD_API_V1_STR}/system-requirements",
    tags=["system-requirements"],
)

reqherd_api_router.include_router(
    softreqs.router,
    prefix=f"{REQHERD_API_V1_STR}/software-requirements",
    tags=["software-requirements"],
)

reqherd_api_router.include_router(
    hardreqs.router,
    prefix=f"{REQHERD_API_V1_STR}/hardware-requirements",
    tags=["hardware-requirements"],
)
