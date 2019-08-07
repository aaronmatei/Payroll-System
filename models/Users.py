from main import db
class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    second_name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    national_id = db.Column(db.String(20),unique=True, nullable=False)
    kra_pin = db.Column(db.String(20),unique=True, nullable=False)
    email = db.Column(db.String(50),unique=True, nullable=False)
    phone = db.Column(db.String(50),unique=True, nullable=False)

    #creating entry
    def instert_into_database(self): #this is an instance method
        db.session.add(self)
        db.session.commit()
