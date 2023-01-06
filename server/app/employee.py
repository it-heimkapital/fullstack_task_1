from . import schemas, models
from sqlalchemy.orm import Session, joinedload
from fastapi import Depends, status, APIRouter
from .database import get_db

router = APIRouter()


@router.get("/get_employees")
def get_employees(db: Session = Depends(get_db), limit: int = 10, page: int = 1):
    """
    Get list of Employees
    """
    skip = (page - 1) * limit

    employees = db.query(models.Employee).options(joinedload(models.Employee.department)).limit(limit).offset(skip).all()

    return {"status": "success", "results": len(employees), "employees": employees}


@router.post("/create_employee", status_code=status.HTTP_201_CREATED)
def create_employee(payload: schemas.Employee, db: Session = Depends(get_db)):
    """
    Create Employees
    """
    employee = models.Employee(**payload.dict())

    # Check first if employee exists with that name and return employee info if exists with message
    response = db.query(models.Employee).filter(models.Employee.first_name == payload.first_name,
                                                models.Employee.last_name == payload.last_name,
                                                models.Employee.department_id == payload.department_id
                                                ).all()
    if response:
        return {"status": "success",
                "msg": "Employee already exists with this name and department",
                "employee": response}
    else:
        db.add(employee)
        db.commit()
        db.refresh(employee)

        return {"status": "success", "employee": employee}


@router.post("/create_department", status_code=status.HTTP_201_CREATED)
def create_department(payload: schemas.Department, db: Session = Depends(get_db)):
    """"
    Create Department
    """
    department = models.Department(**payload.dict())

    # Check first if department exists with that name and return department data if exists with message
    response = db.query(models.Department).filter(models.Department.name == payload.name).all()
    if response:
        return {"status": "success", "msg": "Department already exists with this name", "department": response}
    else:
        db.add(department)
        db.commit()
        db.refresh(department)

        return {"status": "success", "department": department}


@router.get("/get_departments")
def get_departments(db: Session = Depends(get_db), limit: int = 10, page: int = 1):
    """
    Get list of Departments
    """
    skip = (page - 1) * limit
    departments = db.query(models.Department).limit(limit).offset(skip).all()

    return {"status": "success", "results": len(departments), "departments": departments}
