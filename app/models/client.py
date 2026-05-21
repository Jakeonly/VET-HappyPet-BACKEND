from models.person import Person
from uuid import UUID
from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Client(Person):
    __tablename__ = 'Client'

    id: Mapped[UUID] = mapped_column(ForeignKey('Person.id'), primary_key=True)
    registration_date: Mapped[Date] = mapped_column(Date, index=True)
    pets = relationship('Pet', back_populates='client')
    notifications = relationship('Notification', back_populates='client')
    
    __mapper_args__ = {
        'polymorphic_identity': 'client',
    }
