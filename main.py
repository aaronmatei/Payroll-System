# importing Flask class
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from config import Development,Testing,Production
from flask_migrate import Migrate, Manager, MigrateCommand

# instantiating Flask class with instance/object app
app = Flask(__name__)
app.config.from_object(Development)
# app.config.from_object(Production)
# app.config.from_object(Testing)

db = SQLAlchemy(app)
migrate = Migrate(app,db)

# manager = Manager(app)
# manager.add_command('db',MigrateCommand)

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
    return render_template('index.html')

@app.route('/employees/<int:dpt_id>')
def employees(dpt_id):
    departments = DepartmentModel.fetch_all()
    #employees = EmployeeModel.fetch_all()
    this_department = DepartmentModel.fetch_by_id(dpt_id)
    employees = this_department.employees
    dept_id = dpt_id

    return render_template('employees.html', departments= departments, employees=employees, dept_id=dept_id)

@app.route('/departments')
def departments():
    employees = EmployeeModel.fetch_all()
    departments = DepartmentModel.fetch_all()
    return render_template('departments.html', employees= employees, departments=departments)
@app.route('/payrolls/<int:id>')
def payrolls(id):
    this_employee = EmployeeModel.fetch_by_id(id)
    return render_template('payrolls.html', employees = this_employee)


@app.route('/newDepartment', methods=['POST'])
def newDepartment():
    department_name = request.form['department']

    if DepartmentModel.fetch_by_name(department_name):
        flash(department_name + " already exists")
        return redirect(url_for('departments'))

    department = DepartmentModel(dpt_name=department_name) #dpt_name is same as in database
    department.instert_into_database()
    return redirect(url_for('departments'))
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
    departmentID = int(request.form['dpt_name'])
    basic_salary = request.form['basic_salary']
    allowances = request.form['allowances']
    other_deductions = request.form['other_deductions']

    if EmployeeModel.fetch_by_id(national_id):
        flash("That user with national id no " + national_id + " already added")
        return redirect(url_for('employees'))


    employee = EmployeeModel(first_name=first_name,second_name=second_name,gender=gender,
                             national_id=national_id,kra_pin=kra_pin,email=email,departmentID=departmentID,
                             basic_salary = basic_salary,allowances=allowances,other_deductions=other_deductions )
    employee.instert_into_database()

    return redirect(url_for('employees',dpt_id=departmentID))



# run flask
# if __name__ == '__main__':
#     app.run()

