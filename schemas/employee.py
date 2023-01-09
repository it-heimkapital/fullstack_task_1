from typing import Optional
from pydantic import BaseModel


class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    department_id: int


class ShowEmployee(BaseModel):
    first_name: str
    last_name: str
    department_id: int

    class Config:
        orm_mode = True

