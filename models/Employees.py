from main import db
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
    other_deductions = db.Column(db.Float)

    #creating entry
    def instert_into_database(self): #this is an instance method
        db.session.add(self)
        db.session.commit()
     #reading
    @classmethod
    def fetch_by_id(cls,id):
        return cls.query.filter_by(national_id=id).first()

    @classmethod
    def fetch_all(cls):
        return cls.query.all()
