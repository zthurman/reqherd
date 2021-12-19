import logging
import logging.config
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from reqherd.webservice.core.config import settings
from reqherd.webservice.config import SOFTWARE_VERSION
from reqherd.webservice.api.reqherd_api_v1.api import reqherd_api_router


log_file_path = Path(__file__).parent / "reqherd/webservice/logging.conf"
logging.config.fileConfig(log_file_path)


logger = logging.getLogger(__name__)


reqherd = FastAPI(
    title="reqherd API",
    version=SOFTWARE_VERSION,
)

reqherd.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

reqherd.include_router(reqherd_api_router)
