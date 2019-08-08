from main import db
class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    second_name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(50),unique=True, nullable=False)
    phone = db.Column(db.String(50), unique=True, nullable=False)
    national_id = db.Column(db.String(20),unique=True, nullable=False)
    kra_pin = db.Column(db.String(20),unique=True, nullable=False)
    password = db.Column(db.String,nullable=False)
    authenticated = db.Column(db.Boolean, default=False)


    #creating entry
    def instert_into_database(self): #this is an instance method
        db.session.add(self)
        db.session.commit()

    @classmethod
    def fetch_all(cls):
        return cls.query.all()
    @classmethod
    def is_active(self):
        """True, as all users are active."""
        return True

    @classmethod
    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    @classmethod
    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    @classmethod
    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False
