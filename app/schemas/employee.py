from datetime import date
from schemas.person import PersonBase, PersonResponse

class EmployeeBase(PersonBase):
    salary: float
    hire_date: date

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    salary: float | None = None
    hire_date: date | None = None

class EmployeeResponse(EmployeeBase, PersonResponse):
    pass