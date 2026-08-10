# milestone: append-only event repository

from services.event_store.db import SessionLocal
from services.event_store.models import Event


class EventRepository:

    def __init__(self):
        self.db = SessionLocal()

    def append_event(self, event_type: str, payload: dict):
        event = Event(
            event_type=event_type,
            payload=payload,
        )
        self.db.add(event)
        self.db.commit()
        self.db.refresh(event)
        return event

    def list_events(self):
        return self.db.query(Event).order_by(Event.created_at).all()