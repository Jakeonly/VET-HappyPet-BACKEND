from schemas.employee import EmployeeBase, EmployeeResponse

class VeterinarianBase(EmployeeBase):
    specialization: str

class VeterinarianCreate(VeterinarianBase):
    pass

class VeterinarianResponse(VeterinarianBase, EmployeeResponse):
    pass