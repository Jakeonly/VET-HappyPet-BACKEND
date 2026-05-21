from database import Base
from uuid import UUID, uuid4
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship



class Notification(Base):
    __tablename__ = 'Notification'

    id =  Column(UUID, primary_key=True, index=True, default=uuid4)
    dateHour = Column(String, index=True)
    content = Column(String, index=True)
    state = Column(String, index=True)
    client_id = Column(UUID, ForeignKey('Client.id'), nullable=True, index=True)
    appointment_id = Column(UUID, ForeignKey('Appointment.id'), nullable=True, index=True)
    product_id = Column(UUID, ForeignKey('Product.id'), nullable=True, index=True)
    client = relationship('Client', back_populates='notifications')
    appointment = relationship('Appointment', back_populates='notifications')
    product = relationship('Product', back_populates='notifications')
   
    

    def __repr__(self):
        return f"<Notification(dateHour='{self.dateHour}', content='{self.content}', state='{self.state}')>"