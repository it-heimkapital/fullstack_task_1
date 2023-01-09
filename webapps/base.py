from webapps.employee import route_employee
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(route_employee.router, prefix="", tags=["employee-webapp"])
