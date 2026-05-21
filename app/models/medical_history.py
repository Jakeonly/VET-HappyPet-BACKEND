from database import Base
from uuid import UUID, uuid4
from sqlalchemy import Column



class Medical_history(Base):
    __tablename__ = 'Medical_history'

    id =  Column(UUID, primary_key=True, index=True, default=uuid4)
    dateCreation = Column(Date, index=True)
   
    

    def __repr__(self):
        return f"<Medical_history(dateCreation='{self.dateCreation}')>"