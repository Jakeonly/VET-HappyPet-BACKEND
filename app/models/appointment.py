from database import Base
from uuid import UUID, uuid4
from sqlalchemy import Column, Date, String, ForeignKey
from sqlalchemy.orm import relationship



class Appointment(Base):
    __tablename__ = 'Appointment'

    id =  Column(UUID, primary_key=True, index=True, default=uuid4)
    dateHour = Column(Date, index=True)
    state = Column(String, index=True)
    motive = Column(String, index=True)
    pet_id = Column(UUID, ForeignKey('Pet.id'), nullable=False, index=True)
    veterinarian_id = Column(UUID, ForeignKey('Veterinarian.id'), nullable=False, index=True)
    pet = relationship('Pet', back_populates='appointments')
    veterinarian = relationship('Veterinarian', back_populates='appointments')
    medical_history = relationship('Medical_history', back_populates='appointment', uselist=False)
    checklists = relationship('Checklist', back_populates='appointment')
    notifications = relationship('Notification', back_populates='appointment')

    def __repr__(self):
        return f"<Appointment(dateHour='{self.dateHour}', state='{self.state}', motive='{self.motive}')>"