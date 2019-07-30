from app import db
from models.Employees import EmployeeModel
class DepartmentModel(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    dpt_name = db.Column(db.String(50),unique=True, nullable=False)
    employees = db.relationship(EmployeeModel, backref = 'department')
