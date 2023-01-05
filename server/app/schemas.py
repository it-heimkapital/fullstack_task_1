from pydantic import BaseModel
from typing import List


class Department(BaseModel):
    name: str or list

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class Employee(BaseModel):
    first_name: str
    last_name: str
    department_id: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class EmployeeList(BaseModel):
    status: str
    employee: List[Employee]
