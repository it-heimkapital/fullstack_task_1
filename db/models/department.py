from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Department(Base):
    id = Column(Integer, primary_key=True, index=True)
    department_name = Column(String, nullable=False)
    employee = relationship('Employee', back_populates='department')

