from database import Base
from uuid import UUID, uuid4
from sqlalchemy import Column, String, Int



class Notification(Base):
    __tablename__ = 'Notification'

    id =  Column(UUID, primary_key=True, index=True, default=uuid4)
    dateHour = Column(String, index=True)
    content = Column(String, index=True)
    state = Column(String, index=True)
   
    

    def __repr__(self):
        return f"<Notification(dateHour='{self.dateHour}', content='{self.content}', state='{self.state}')>"