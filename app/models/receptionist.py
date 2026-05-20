from models.employee import Employee
from uuid import UUID
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class Receptionist(Employee):
    __tablename__ = 'Receptionist'

    id: Mapped[UUID] = mapped_column(ForeignKey('Employee.id'), primary_key=True)
    
    __mapper_args__ = {
        'polymorphic_identity': 'receptionist',
    }
