from database import Base
from uuid import UUID, uuid4
from sqlalchemy import Column, Int, String



class SaleDetail(Base):
    __tablename__ = 'SaleDetail'

    
    quantity = Column(Int, index=True)
    subQuantity = Column(Decimal, index=True)
    

    def __repr__(self):
        return f"<SaleDetail(quantity='{self.quantity}', subQuantity='{self.subQuantity}')>"