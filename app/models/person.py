from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
from uuid import uuid4, UUID


class Person(Base):
    __tablename__ = 'Person'

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    phone_number: Mapped[str] = mapped_column(String, index=True)
    address: Mapped[str] = mapped_column(String, index=True)
    type: Mapped[str] = mapped_column(String)

    __mapper_args__ = {
        'polymorphic_identity': 'person',
        'polymorphic_on': type
    }

    def __repr__(self):
        return f"<Person(name='{self.name}', email='{self.email}', phone_number='{self.phone_number}', address='{self.address}')>"
