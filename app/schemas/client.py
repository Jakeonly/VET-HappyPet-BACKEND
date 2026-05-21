from datetime import date
from schemas.person import PersonBase, PersonResponse

class ClientBase(PersonBase):
    registration_date: date

class ClientCreate(ClientBase):
    pass

class ClientUpdate(ClientBase):
    registration_date: date | None = None

class ClientResponse(ClientBase, PersonResponse):
    pass 