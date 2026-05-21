from database import Base
from uuid import UUID, uuid4
from sqlalchemy import Column, Date, Double, ForeignKey
from sqlalchemy.orm import relationship



class Sale(Base):
    __tablename__ = 'Sale'

    id =  Column(UUID, primary_key=True, index=True, default=uuid4)
    dateEmision = Column(Date, index=True)
    total = Column(Double, index=True)
    financial_report_id = Column(UUID, ForeignKey('Financial_report.id'), nullable=False, index=True)
    financial_report = relationship('Financial_report', back_populates='sales')
    details = relationship('SaleDetail', back_populates='sale')
    

    def __repr__(self):
        return f"<Sale(dateEmision='{self.dateEmision}', total='{self.total}')>"