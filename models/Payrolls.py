from app import db
class PayrollModel(db.Model):
    __tablename__ = 'payrolls'
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    payroll_month = db.Column(db.Integer, nullable=False)
    gross_salary = db.Column(db.Float)
    nssf_deductions = db.Column(db.Float)
    nhif_deductions = db.Column(db.Float)
    PAYE = db.Column(db.Float)
    taxable_income= db.Column(db.Float)
    overtime = db.Column(db.Float)
    net_salary = db.Column(db.Float)

