# milestone: database connection for event store

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from services.common.config import settings


engine = create_engine(settings.POSTGRES_URL)
SessionLocal = sessionmaker(bind=engine)