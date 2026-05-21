from database import Base
from uuid import UUID, uuid4
from sqlalchemy import Column, Date, String



class Appointment(Base):
    __tablename__ = 'Appointment'

    id =  Column(UUID, primary_key=True, index=True, default=uuid4)
    dateHour = Column(Date, index=True)
    state = Column(String, index=True)
    motive = Column(String, index=True)

    def __repr__(self):
        return f"<Appointment(dateHour='{self.dateHour}', state='{self.state}', motive='{self.motive}')>"