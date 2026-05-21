from database import Base
from uuid import UUID, uuid4
from sqlalchemy import Column, Integer, ForeignKey, Numeric
from sqlalchemy.orm import relationship



class SaleDetail(Base):
    __tablename__ = 'SaleDetail'

    id = Column(UUID, primary_key=True, index=True, default=uuid4)
    sale_id = Column(UUID, ForeignKey('Sale.id'), nullable=False, index=True)
    product_id = Column(UUID, ForeignKey('Product.id'), nullable=False, index=True)
    
    quantity = Column(Integer, index=True)
    subQuantity = Column(Numeric, index=True)
    sale = relationship('Sale', back_populates='details')
    product = relationship('Product', back_populates='details')
    

    def __repr__(self):
        return f"<SaleDetail(quantity='{self.quantity}', subQuantity='{self.subQuantity}')>"