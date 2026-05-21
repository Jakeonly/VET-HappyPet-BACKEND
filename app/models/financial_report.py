from database import Base
from uuid import UUID, uuid4
from sqlalchemy import Column, Date, Numeric, ForeignKey
from sqlalchemy.orm import relationship



class Financial_report(Base):
    __tablename__ = 'Financial_report'

    id =  Column(UUID, primary_key=True, index=True, default=uuid4)
    dateStart = Column(Date, index=True)
    dateEnd = Column(Date, index=True)
    income = Column(Numeric, index=True)
    expenses = Column(Numeric, index=True)
    sales = relationship('Sale', back_populates='financial_report')
   
    

    def __repr__(self):
        return f"<Financial_report(dateStart='{self.dateStart}', dateEnd='{self.dateEnd}', income='{self.income}, expenses='{self.expenses}')>"
