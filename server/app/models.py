from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL
from sqlalchemy import func, ForeignKey, UniqueConstraint
from sqlalchemy import Column, String, TIMESTAMP

from app.database import Base


class Department(Base):
    __tablename__ = "department"
    id = Column(GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL)
    name = Column(String, nullable=False, unique=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), default=None, onupdate=func.now())


class Employee(Base):
    __tablename__ = "Employee"
    id = Column(GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    department_id = Column(GUID, ForeignKey("department.id"))
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), default=None, onupdate=func.now())

    __table_args__ = (UniqueConstraint("first_name", "last_name", "department_id", name="_employee_department_unique"),
                      )


