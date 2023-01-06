import logging
import sys

from app import models
from app import schemas
from app.database import get_db

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

db = next(get_db())


def create_initial_department(department_list: list) -> None:
    for department in department_list:
        payload = schemas.Department(name=department)
        result = db.query(models.Department).filter(models.Department.name == department).all()
        if result:
            logging.info(f"Department already exists with name: {department}")
            continue
        department = models.Department(**payload.dict())
        db.add(department)
        db.commit()
        logging.info(f"Inserted Department with name: {department}")


if __name__ == '__main__':
    """
    Department name can be passed in argument as comma separated string.
    If not provided in input hardcoded default list will be used. i.e ["Sales", "Ops", "IT"]
    e.g.: python3 -m utils.create_department "Sales,Ops,IT"
    """
    input = sys.argv
    if len(input) > 1:
        department_list = input[1].split(",")
    else:
        department_list = ["Sales", "Ops", "IT"]  # this list can be updated

    create_initial_department(department_list)
