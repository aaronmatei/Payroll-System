# importing Flask class
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Development,Testing

# instantiating Flask class with instance/object app
app = Flask(__name__)
app.config.from_object(Development)
# app.config.from_object(Testing)
db = SQLAlchemy(app)
from models.Employees import EmployeeModel
from models.Departments import DepartmentModel
from models.Payrolls import PayrollModel

@app.before_first_request     #before any request from user, run this first(create tables)
def createTables():
    db.create_all()

# registering a route
@app.route('/')
# when this route is visited, launch this method
def home():
    return render_template('flask.html')

# run flask
# if __name__ == '__main__':
#     app.run()

