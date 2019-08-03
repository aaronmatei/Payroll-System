from main import db
from models.Employees import EmployeeModel
class DepartmentModel(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    dpt_name = db.Column(db.String(50),unique=True, nullable=False)
    employees = db.relationship(EmployeeModel, backref = 'department')

    #creating entry
    def instert_into_database(self): #this is an instance method
        db.session.add(self)
        db.session.commit()
     #reading
    @classmethod
    def fetch_by_name(cls,name):
        return cls.query.filter_by(dpt_name=name).first()

    @classmethod
    def fetch_all(cls):
        return cls.query.all()
