from api import db


class Department(db.Model):
    """
    db model class for Department
    department class has relationship with employee using backref
    """

    __tablename__ = "department"
    id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(25), unique=True, nullable=False)
    employees = db.relationship("Employee", backref="department")


class Employee(db.Model):
    """
    db model class for employee
    """

    __tablename__ = "employee"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), unique=False, nullable=False)
    last_name = db.Column(db.String(25), unique=False, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey("department.id"))
