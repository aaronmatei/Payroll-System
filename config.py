class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'heyyou!'
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:29094964@127.0.0.1:5432/payroll'
    environment = 'Development'
    DEBUG = True

class Development (Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:29094964@127.0.0.1:5432/payroll'
    environment = 'Development'
    DEBUG = True
class Testing (Config):
    # SQLALCHEMY_DATABASE_URI = ''
    DEBUG = False
class Production (Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://my_company:29094964@192.0.10.1:5432/payroll'
    DEBUG = False
    environment = 'Production'