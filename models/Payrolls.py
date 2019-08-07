from main import db
class PayrollsModel(db.Model):
    __tablename__ = 'payrolls'
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    dept_name = db.Column(db.String(50), db.ForeignKey('departments.dpt_name'))
    payroll_month = db.Column(db.String(50), nullable=False)
    gross_salary = db.Column(db.Float)
    nssf_deductions = db.Column(db.Float)
    nhif_deductions = db.Column(db.Float)
    taxable_income = db.Column(db.Float)
    PAYE = db.Column(db.Float)
    overtime = db.Column(db.Float)
    salary_advance = db.Column(db.Float)
    other_deductions = db.Column(db.Float)
    net_salary = db.Column(db.Float)


    #creating entry
    def instert_into_database(self): #this is an instance method
        db.session.add(self)
        db.session.commit()
    @classmethod
    def fetch_by_id(cls,emp_id):
        return cls.query.filter_by(employee_id=emp_id).first()

    @classmethod
    def fetch_all(cls):
        return cls.query.all()

