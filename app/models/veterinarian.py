from models.employee import Employee
from uuid import UUID
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Veterinarian(Employee):
    __tablename__ = 'Veterinarian'

    id: Mapped[UUID] = mapped_column(ForeignKey('Employee.id'), primary_key=True)
    specialization: Mapped[str] = mapped_column(String, index=True)
    appointments = relationship('Appointment', back_populates='veterinarian')

    __mapper_args__ = {
        'polymorphic_identity': 'veterinarian',
    }
