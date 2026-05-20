from models.person import Person
from uuid import UUID
from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class Employee(Person):
    __tablename__ = 'Employee'

    id: Mapped[UUID] = mapped_column(ForeignKey('Person.id'), primary_key=True)
    salary: Mapped[float] = mapped_column(float, index=True)
    hire_date: Mapped[Date] = mapped_column(Date, index=True)
    
    __mapper_args__ = {
        'polymorphic_identity': 'employee',
    }
