from database import Base
from uuid import UUID, uuid4
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship



class Pet(Base):
    __tablename__ = 'Pet'

    id =  Column(UUID, primary_key=True, index=True, default=uuid4)
    name = Column(String, index=True)
    age = Column(Integer, index=True)
    specie = Column(String, index=True)
    race = Column(String, index=True)
    sex = Column(String, index=True)
    client_id = Column(UUID, ForeignKey('Client.id'), nullable=False, index=True)
    client = relationship('Client', back_populates='pets')
    appointments = relationship('Appointment', back_populates='pet')
    medical_history = relationship('Medical_history', back_populates='pet', uselist=False)
    

    def __repr__(self):
        return f"<Pet(name='{self.name}', age='{self.age}', specie='{self.specie}, race='{self.race}, sex='{self.sex}')>"
