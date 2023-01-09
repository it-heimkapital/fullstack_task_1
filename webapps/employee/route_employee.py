from fastapi import APIRouter
from fastapi import Request, Depends, responses, status
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db.repository.employee import list_employees
from db.session import get_db
from webapps.employee.forms import EmployeeCreateForm
from db.repository.employee import create_new_employee
from schemas.employee import EmployeeCreate

templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/")
async def home(request: Request, db: Session = Depends(get_db)):
    employees = list_employees(db=db)
    return templates.TemplateResponse(
        "general_pages/homepage.html", {"request": request, "employees": employees}
    )


@router.get("/post-an-employee/")
def create_employee(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("employee/create_employee.html", {"request": request})


@router.post("/post-an-employee/")
async def create_employee(request: Request, db: Session = Depends(get_db)):
    form = EmployeeCreateForm(request)
    await form.load_data()
    if form.is_valid():
        try:
            employee = EmployeeCreate(**form.__dict__)
            employee = create_new_employee(employee=employee, db=db)
            return responses.RedirectResponse(
                f"/", status_code=status.HTTP_302_FOUND
            )
        except Exception as e:
            print(e)
            form.__dict__.get("errors").append(
                "Something went wrong, In case problem persists please contact us."
            )
            return templates.TemplateResponse("employee/create_employee.html", form.__dict__)
    return templates.TemplateResponse("employee/create_employee.html", form.__dict__)
