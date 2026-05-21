
from pydantic import BaseModel
from sqlalchemy import UUID


class PersonBase(BaseModel):
    name: str
    email: str
    phone_number: str
    address: str
    type: str

class PersonCreate(PersonBase):
    pass

class PersonUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    phone_number: str | None = None
    address: str | None = None
    type: str | None = None

class PersonResponse(PersonBase):
    id: UUID  

    model_config = {
        "from_attributes": True
    }

