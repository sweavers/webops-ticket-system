from sqlalchemy import Column, Integer, String, DateTime, Float, Date
from application import db

class Tickets(db.Model):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True)
    project = Column(String(64), nullable=False)
    title = Column(String(120), nullable=False)
    description = Column(String(120), nullable=False)
    contact = Column(String(120), nullable=False)
    priority = Column(String(120), nullable=False)

    def __init__(self, project, title, description, contact, priority):
        self.project = project
        self.title = title
        self.description = description
        self.contact = contact
        self.priority = priority
