from database import Base
from uuid import UUID, uuid4
from sqlalchemy import Column, Date



class Sale(Base):
    __tablename__ = 'Sale'

    id =  Column(UUID, primary_key=True, index=True, default=uuid4)
    dateEmision = Column(Date, index=True)
    total = Column(Double, index=True)
    

    def __repr__(self):
        return f"<Sale(dateEmision='{self.dateEmision}', total='{self.total}')>"