# importing Flask class

import bcrypt as bcrypt
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import login_manager, login_user
from flask_sqlalchemy import SQLAlchemy
from config import Development,Testing,Production
from flask_migrate import Migrate, Manager, MigrateCommand
from resources.payroll import Payroll






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
from models.Users import UserModel
from models.Payrolls import PayrollsModel
#TODO: read flask-migrate
@app.before_first_request     #before any request from user, run this first(create tables)
def createTables():
    # db.drop_all()
    db.create_all()

# registering a route
@app.route('/')
# when this route is visited, launch this method

def home():
    return render_template('index.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/login',methods=['POST','GET'])
def login():
#     print (db)
#     # form = LoginForm()
#     if form.validate_on_submit():
#         user = UserModel.fetch_all()
#         password = request.form['password']
#         if user:
#             if bcrypt.check_password_hash(user.password, password):
#                 user.authenticated = True
#                 db.session.add(user)
#                 db.session.commit()
#                 login_user(user, remember=True)
#                 return redirect(url_for("home"))
    return render_template("login.html")


@app.route("/logout", methods=["GET"])


@app.route('/employees/<int:dpt_id>')
def employees(dpt_id):

    this_department = DepartmentModel.fetch_by_id(dpt_id)
    # employees = this_department.employees
    departments = DepartmentModel.fetch_all()

    return render_template('employees.html', this_department=this_department,departments=departments)

@app.route('/departments')
def departments():
    employees = EmployeeModel.fetch_all()
    departments = DepartmentModel.fetch_all()
    return render_template('departments.html', employees= employees, departments=departments)

@app.route('/payrolls/<int:emp_id>')
def payrolls(emp_id):
    # this_employee = EmployeeModel.fetch_by_id(emp_id)
    # emp_payroll = PayrollsModel.fetch_all()
    this_employee = EmployeeModel.fetch_by_id(emp_id)

    return render_template('payrolls.html', this_employee=this_employee)

@app.route('/newPayroll/<emp_id>', methods=['POST'])
def newPayroll(emp_id):
    this_employee = EmployeeModel.fetch_by_id(emp_id)
    payroll = Payroll(this_employee.first_name+this_employee.second_name,this_employee.basic_salary, this_employee.allowances)

    payroll_month = request.form['payroll_month']
    gross_salary = payroll.gross_salary
    employee_id = emp_id
    dept_name= request.form['dept_name']
    nssf_deductions = payroll.nssf_deductions
    nhif_deductions = payroll.nhif_deductions
    PAYE = payroll.payee
    taxable_income = payroll.taxable_income
    overtime = request.form['overtime']
    salary_advance = request.form['salary_advance']
    other_deductions = request.form['other_deductions']
    net_salary = payroll.net_salary

    emp_payroll = PayrollsModel(employee_id=employee_id,dept_name=dept_name,payroll_month=payroll_month,gross_salary=gross_salary,
                                nssf_deductions=nssf_deductions,nhif_deductions=nhif_deductions,taxable_income=taxable_income,PAYE=PAYE,
                                overtime=overtime,salary_advance=salary_advance,other_deductions=other_deductions,net_salary=net_salary)
    emp_payroll.instert_into_database()

    return redirect(url_for('payrolls',emp_id=emp_id))


@app.route('/newUser',methods=['POST'])
def newUser():
    first_name = request.form['first_name']
    second_name = request.form['second_name']
    gender = request.form['gender']
    national_id = request.form['national_id']
    kra_pin = request.form['kra_pin']
    phone = request.form['phone']
    email = request.form['email']
    password = request.form['password']

    user = UserModel(first_name=first_name,second_name=second_name,gender=gender,
                             national_id=national_id,kra_pin=kra_pin,phone=phone,email=email,password=password)
    user.instert_into_database()
    return redirect(url_for('login'))

# @app.route('/login', methods=['POST'])
# def login():
#     pass
#     return render_template('index.html')


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


    if EmployeeModel.fetch_by_id(national_id):
        flash("That user with national id no " + national_id + " already added")
        return redirect(url_for('employees'))


    employee = EmployeeModel(first_name=first_name,second_name=second_name,gender=gender,
                             national_id=national_id,kra_pin=kra_pin,email=email,departmentID=departmentID,
                             basic_salary = basic_salary,allowances=allowances)
    employee.instert_into_database()

    return redirect(url_for('employees',dpt_id=departmentID))

@app.route('/editEmployee/<int:id>', methods=['POST'])
def editEmployee(id):
    first_name = request.form['first_name']
    second_name = request.form['second_name']
    gender = request.form['gender']
    national_id = request.form['national_id']
    kra_pin = request.form['kra_pin']
    email = request.form['email']
    departmentID = int(request.form['dpt_name'])
    basic_salary = request.form['basic_salary']
    allowances = request.form['allowances']

    if gender == "na":
        gender=None
    if departmentID == "0":
        departmentID=None

    EmployeeModel.update_by_id(id=id,first_name=first_name,second_name=second_name,gender=gender,national_id=national_id,
                               kra_pin=kra_pin,email=email,departmentID=departmentID,basic_salary=basic_salary,allowances=allowances)
    this_emp = EmployeeModel.fetch_by_id(emp_id=id)
    this_dept = this_emp.department

    return redirect(url_for('employees',dpt_id=this_dept.id))

@app.route('/deleteEmployee/<int:id>')
def deleteEmployee(id):
    this_emp = EmployeeModel.fetch_by_id(emp_id=id)
    this_dept = this_emp.department
    EmployeeModel.delete_by_id(id=id)

    return redirect(url_for('employees',dpt_id=this_dept.id))


# run flask
# if __name__ == '__main__':
#     app.run()

