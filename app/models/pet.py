from database import Base
from uuid import UUID, uuid4
from sqlalchemy import Column, String, Int



class Pet(Base):
    __tablename__ = 'Pet'

    id =  Column(UUID, primary_key=True, index=True, default=uuid4)
    name = Column(String, index=True)
    age = Column(Int, index=True)
    specie = Column(String, index=True)
    race = Column(String, index=True)
    sex = Column(String, index=True)
    

    def __repr__(self):
        return f"<Pet(name='{self.name}', age='{self.age}', specie='{self.specie}, race='{self.race}, sex='{self.sex}')>"
