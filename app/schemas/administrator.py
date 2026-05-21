from schemas.employee import EmployeeBase, EmployeeResponse

class AdministratorBase(EmployeeBase):
    pass

class AdministratorCreate(AdministratorBase):
    pass

class administratorUpdate(AdministratorBase):
    pass

class AdministratorResponse(AdministratorBase, EmployeeResponse):
    pass