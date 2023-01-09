from typing import List
from typing import Optional
from fastapi import Request


class EmployeeCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.first_name: Optional[str] = None
        self.last_name: Optional[str] = None
        self.department_id: Optional[int] = None

    async def load_data(self):
        form = await self.request.form()
        self.first_name = form.get("first_name")
        self.last_name = form.get("last_name")
        self.department_id = form.get("department_id")

    def is_valid(self):
        if not self.first_name or not len(self.first_name) >= 2:
            self.errors.append("A valid name is required")
        if not self.last_name or not len(self.last_name) >= 2:
            self.errors.append("A valid last name is required")
        if not self.department_id:
            self.errors.append("Department is not chosen")
        if not self.errors:
            return True
        return False
