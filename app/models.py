from app import db
from dataclasses import dataclass


@dataclass()
class User(db.Model):
    id: int
    first_name: str
    last_name: str
    username: str
    company: str
    contact_no: str
    email: str

    __tablename__ = 'demo_users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    username = db.Column(db.String(64))
    company = db.Column(db.String(64))
    contact_no = db.Column(db.String(64))
    email = db.Column(db.String(120), index=True, unique=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

