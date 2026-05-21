from database import Base
from uuid import UUID, uuid4
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship



class Checklist(Base):
    __tablename__ = 'Checklist'

    id =  Column(UUID, primary_key=True, index=True, default=uuid4)
    diagnosis = Column(String, index=True)
    treatment = Column(String, index=True)
    services = Column(String, index=True)
    appointment_id = Column(UUID, ForeignKey('Appointment.id'), nullable=False, index=True)
    appointment = relationship('Appointment', back_populates='checklists')
    
   
    

    def __repr__(self):
        return f"<Checklist(diagnosis='{self.diagnosis}', treatment='{self.treatment}', services='{self.services}')>"
