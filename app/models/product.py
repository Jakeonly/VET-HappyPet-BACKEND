from database import Base
from uuid import UUID, uuid4
from sqlalchemy import Column, Date, String, Int



class Product(Base):
    __tablename__ = 'Product'

    id =  Column(UUID, primary_key=True, index=True, default=uuid4)
    name = Column(String, index=True)
    category = Column(String, index=True)
    price = Column(Decimal, index=True)
    expire = Column(Date, index=True)
    stock = Column(Int, index=True)
    

    def __repr__(self):
        return f"<Product(name='{self.name}', category='{self.category}', price='{self.price}, expire='{self.expire},stock='{self.stock}')>"