from models.person import Person
from uuid import UUID
from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class Client(Person):
    __tablename__ = 'Client'

    id: Mapped[UUID] = mapped_column(ForeignKey('Person.id'), primary_key=True)
    registration_date: Mapped[Date] = mapped_column(Date, index=True)
    
    __mapper_args__ = {
        'polymorphic_identity': 'client',
    }
