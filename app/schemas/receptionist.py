from schemas.employee import EmployeeBase, EmployeeResponse

class ReceptionistBase(EmployeeBase):
    pass

class ReceptionistCreate(ReceptionistBase):
    pass

class ReceptionistUpdate(ReceptionistBase):
    pass

class ReceptionistResponse(ReceptionistBase, EmployeeResponse):
    pass