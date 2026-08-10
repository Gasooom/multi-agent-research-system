# milestone: initialize database schema

from services.event_store.models import Base
from services.event_store.db import engine

Base.metadata.create_all(bind=engine)