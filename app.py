# importing Flask class
from flask import Flask, render_template, request, redirect, url_for, flash
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
#TODO: read flask-migrate
@app.before_first_request     #before any request from user, run this first(create tables)
def createTables():
    #db.drop_all()
    db.create_all()

# registering a route
@app.route('/')
# when this route is visited, launch this method

def home():
    departments = DepartmentModel.fetch_all()
    return render_template('flask.html',departments= departments)

@app.route('/employees/<int:dpt_id>')
def employees(dpt_id):
    departments = DepartmentModel.fetch_all()
    return render_template('employees.html', departments= departments)


@app.route('/newDepartment', methods=['POST'])
def newDepartment():
    department_name = request.form['department']
    if DepartmentModel.fetch_by_name(department_name):
        flash(department_name + "already exists")
        return redirect(url_for('home'))

    department = DepartmentModel(dpt_name=department_name) #dpt_name is same as in database
    department.instert_into_database()
    return redirect(url_for('home'))
    # print(data)
    # department_name = data['department']
@app.route('/newEmployee', methods=['POST'])
def newEmployee():
    first_name = request.form['first_name']
    second_name = request.form['second_name']
    gender = request.form['gender']
    national_id = request.form['national_id']
    kra_pin = request.form['kra_pin']
    email = request.form['email']
    departmentID = request.form['dpt_name']
    basic_salary = request.form['basic_salary']
    allowances = request.form['allowances']
    other_deductions = request.form['other_deductions']

# run flask
# if __name__ == '__main__':
#     app.run()

