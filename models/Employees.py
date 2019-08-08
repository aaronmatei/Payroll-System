from main import db
from models.Payrolls import PayrollsModel
class EmployeeModel(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    second_name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    national_id = db.Column(db.String(20),unique=True, nullable=False)
    kra_pin = db.Column(db.String(20),unique=True, nullable=False)
    email = db.Column(db.String(50),unique=True, nullable=False)
    departmentID = db.Column(db.Integer, db.ForeignKey('departments.id'))
    basic_salary = db.Column(db.Float)
    allowances = db.Column(db.Float)

    emp_payrolls = db.relationship(PayrollsModel, backref='employee')

    #creating entry
    def instert_into_database(self): #this is an instance method
        db.session.add(self)
        db.session.commit()
     #reading
    @classmethod
    def fetch_by_id(cls, emp_id):
        return cls.query.filter_by(id=emp_id).first()

    @classmethod
    def fetch_all(cls):
        return cls.query.all()

    #update record
    @classmethod
    def update_by_id(cls,id,first_name=None,second_name=None,gender=None,national_id=None,kra_pin=None,email=None,departmentID=None,basic_salary=None,allowances=None):
        record = cls.fetch_by_id(emp_id=id)
        if first_name:
            record.first_name=first_name
        if second_name:
            record.second_name = second_name
        if gender:
            record.gender=gender
        if national_id:
            record.national_id = national_id
        if kra_pin:
            record.kra_pin=kra_pin
        if email:
            record.email = email
        if departmentID:
            record.departmentID=departmentID
        if basic_salary:
            record.basic_salary = basic_salary
        if allowances:
            record.allowances = allowances

        db.session.commit()
        return True

    #delete record
    @classmethod
    def delete_by_id(cls,id):
        record = cls.query.filter_by(id=id)
        record.delete()
        db.session.commit()
        return True




