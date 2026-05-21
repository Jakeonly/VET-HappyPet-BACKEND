from database import Base
from uuid import UUID, uuid4
from sqlalchemy import Column, String, Int



class Checklist(Base):
    __tablename__ = 'Checklist'

    id =  Column(UUID, primary_key=True, index=True, default=uuid4)
    diagnosis = Column(String, index=True)
    treatment = Column(String, index=True)
    services = Column(String, index=True)
    
   
    

    def __repr__(self):
        return f"<Checklist(diagnosis='{self.diagnosis}', treatment='{self.treatment}', services='{self.services}')>"
