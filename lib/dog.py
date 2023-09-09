from models import Dog  # Import your Dog model from models.py
from sqlalchemy.orm import Session, base

def create_table(base):
    base.metadata.create_all()

def save(session: Session, dog: Dog):
    session.add(dog)
    session.commit()

def get_all(session: Session):
    return session.query(Dog).all()

def find_by_name(session: Session, name: str):
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session: Session, id: int):
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session: Session, name: str, breed: str):
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session: Session, dog: Dog, new_breed: str):
    dog.breed = new_breed
    session.commit()
