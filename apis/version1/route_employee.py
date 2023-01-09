from typing import List

from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from schemas.employee import EmployeeCreate, ShowEmployee
from db.session import get_db
from db.repository.employee import create_new_employee, retrieve_employee, list_employees

router = APIRouter()


@router.post("/create", response_model=ShowEmployee)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    employee = create_new_employee(employee=employee, db=db)
    return employee


@router.get('/get/{id}', response_model=ShowEmployee)
def read_employee(id: int, db: Session = Depends(get_db)):
    employee = retrieve_employee(id=id, db=db)
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with this id {id} does not exist")
    return employee


@router.get('/all', response_model=List[ShowEmployee])
def read_employees(db: Session = Depends(get_db)):
    employees = list_employees(db=db)
    return employees

