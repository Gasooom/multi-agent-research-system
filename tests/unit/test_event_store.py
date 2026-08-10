# milestone: event store basic test

from services.event_store.repository import EventRepository


def test_append_event():
    repo = EventRepository()
    event = repo.append_event("TestEvent", {"key": "value"})

    assert event.event_type == "TestEvent"
    assert event.payload["key"] == "value"