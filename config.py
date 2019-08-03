class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'heyyou!'
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:29094964@127.0.0.1:5432/payroll'
    environment = 'Development'
    DEBUG = True

class Development (Config):
    # SQLALCHEMY_DATABASE_URI = 'postgres://postgres:29094964@127.0.0.1:5432/payroll'
    environment = 'Development'
    DEBUG = True
class Testing (Config):
    # SQLALCHEMY_DATABASE_URI = ''
    DEBUG = False
class Production (Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://vsrhdeqzlaautl:a7fdfc1bb3f98349e8b0609e96b5141ab5dfb0daafa7a30fa3c38a174d831aff@ec2-54-221-215-228.compute-1.amazonaws.com:5432/d53fueuquhq8e1'
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    environment = 'Production'