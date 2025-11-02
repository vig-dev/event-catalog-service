from sqlalchemy.orm import Session
from app.models.event import Event

# 🔹 Get all events
def get_all_events(db: Session):
    return db.query(Event).all()

# 🔹 Get event by ID
def get_event_by_id(db: Session, event_id: int):
    return db.query(Event).filter(Event.event_id == event_id).first()

# 🔹 Add new event
def create_event(db: Session, event_data):
    new_event = Event(**event_data.dict())
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event

# 🔹 Delete event
def delete_event(db: Session, event_id: int):
    event = db.query(Event).filter(Event.event_id == event_id).first()
    if event:
        db.delete(event)
        db.commit()
        return True
    return False
