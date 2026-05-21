from database import Base
from uuid import UUID, uuid4
from sqlalchemy import Column, Date, String, Integer, ForeignKey, Numeric
from sqlalchemy.orm import relationship



class Product(Base):
    __tablename__ = 'Product'

    id =  Column(UUID, primary_key=True, index=True, default=uuid4)
    name = Column(String, index=True)
    category = Column(String, index=True)
    price = Column(Numeric, index=True)
    expire = Column(Date, index=True)
    stock = Column(Integer, index=True)
    details = relationship('SaleDetail', back_populates='product')
    notifications = relationship('Notification', back_populates='product')
    

    def __repr__(self):
        return f"<Product(name='{self.name}', category='{self.category}', price='{self.price}, expire='{self.expire},stock='{self.stock}')>"