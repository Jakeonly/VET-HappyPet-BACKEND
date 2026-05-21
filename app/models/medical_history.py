from database import Base
from uuid import UUID, uuid4
from sqlalchemy import Column, Date, ForeignKey
from sqlalchemy.orm import relationship



class Medical_history(Base):
    __tablename__ = 'Medical_history'

    id =  Column(UUID, primary_key=True, index=True, default=uuid4)
    dateCreation = Column(Date, index=True)
    pet_id = Column(UUID, ForeignKey('Pet.id'), nullable=False, unique=True, index=True)
    appointment_id = Column(UUID, ForeignKey('Appointment.id'), nullable=True, unique=True, index=True)
    pet = relationship('Pet', back_populates='medical_history')
    appointment = relationship('Appointment', back_populates='medical_history')
   
    

    def __repr__(self):
        return f"<Medical_history(dateCreation='{self.dateCreation}')>"