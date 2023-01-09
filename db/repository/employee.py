from sqlalchemy.orm import Session
from schemas.employee import EmployeeCreate
from db.models.employee import Employee


def create_new_employee(employee: EmployeeCreate, db: Session):
    employee = Employee(first_name=employee.first_name,
                        last_name=employee.last_name,
                        department_id=employee.department_id
                        )
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee


def retrieve_employee(id: int, db: Session):
    item = db.query(Employee).get(id)
    return item


def list_employees(db: Session):
    employees = db.query(Employee).all()
    return employees
