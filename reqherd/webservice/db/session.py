from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..config import reqherd_settings

engine = create_engine(reqherd_settings(), pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
