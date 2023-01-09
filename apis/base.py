from fastapi import APIRouter
from apis.version1 import route_general_pages
from apis.version1 import route_employee


api_router = APIRouter()
api_router.include_router(route_employee.router, prefix="/employee", tags=["employee"])
