'''Create a class called Payroll whose major task is to calculate an individual’s
Net Salary by getting the inputs basic salary and benefits.
Create 5 different class methods which will
calculate the payee (i.e. Tax), NHIFDeductions, NSSFDeductions, grossSalary and netSalary.'''

class Payroll:
    emp_name= ""
    KRA_PIN =""
    id_number = 0
    basic_salary = 0.00
    allowances = 0.00
    gross_salary = 0.00
    taxable_income = 0.00
    # pension_contribution = 0.06
    pension = 0.00
    nssf_deductions = 0.00
    nhif_deductions = 0.00
    payee = 0.00
    other_deductions = 0.00
    personal_relief = 1408.00
    total_deductions = 0.00
    net_salary = 0.00

    def __init__(self,emp_name,KRA_PIN,id_number,basic_salary,allowances,other_deductions):
        self.emp_name = emp_name
        self.KRA_PIN = KRA_PIN
        self.id_number = id_number
        self.basic_salary= basic_salary
        self.allowances = allowances
        self.other_deductions = other_deductions
        # Payroll.pension(self)
        Payroll.grossSalary(self)
        Payroll.nssfDeductions(self)
        Payroll.taxableIncome(self)
        Payroll.nhifDeductions(self)
        Payroll.paye(self)
        Payroll.totalDeductions(self)
        Payroll.netSalary(self)

    # def pension(self):
    #     self.pension = self.basic_salary * self.pension_contribution


    def grossSalary(self):
        self.gross_salary = self.basic_salary + self.allowances
        # return self.gross_salary

    def nssfDeductions(self):
        if self.basic_salary > 0 and self.basic_salary <= 6000:
            self.nssf_deductions = 360
        elif self.basic_salary >=6001 and self.basic_salary <= 18000:
            self.nssf_deductions = 6/100 * self.basic_salary
        elif self.basic_salary > 18000:
            self.nssf_deductions = 1080
        # return self.nssf_deductions

    def taxableIncome(self):
        if self.pension > 20000.00:
            self.taxable_income = self.gross_salary - 20000.00-self.nssf_deductions
        else:
            self.taxable_income=self.gross_salary-self.pension-self.nssf_deductions
        # return self.taxable_income

    def nhifDeductions(self):
        if self.gross_salary > 0 and self.gross_salary <= 5999:
            self.nhif_deductions = 150
        elif self.gross_salary >=6000 and self.gross_salary <= 7999:
            self.nhif_deductions = 300
        elif self.gross_salary >= 8000 and self.gross_salary <= 11999:
            self.nhif_deductions = 400
        elif self.gross_salary >= 12000 and self.gross_salary <= 14999:
            self.nhif_deductions = 500
        elif self.gross_salary >= 15000 and self.gross_salary <= 19999:
            self.nhif_deductions = 600
        elif self.gross_salary >= 20000 and self.gross_salary <= 24999:
            self.nhif_deductions = 750
        elif self.gross_salary >= 25000 and self.gross_salary <= 29999:
            self.nhif_deductions = 850
        elif self.gross_salary >=30000 and self.gross_salary <= 34999:
            self.nhif_deductions = 900
        elif self.gross_salary >= 35000 and self.gross_salary <= 39999:
            self.nhif_deductions = 950
        elif self.gross_salary >= 40000 and self.gross_salary <= 44999:
            self.nhif_deductions = 1000
        elif self.gross_salary >= 45000 and self.gross_salary <= 49999:
            self.nhif_deductions = 1100
        elif self.gross_salary >= 50000 and self.gross_salary <= 5999:
            self.nhif_deductions = 1200
        elif self.gross_salary >= 60000 and self.gross_salary <= 69999:
            self.nhif_deductions = 1300
        elif self.gross_salary >= 70000 and self.gross_salary <= 79999:
            self.nhif_deductions = 1400
        elif self.gross_salary >= 80000 and self.gross_salary <= 89999:
            self.nhif_deductions = 1500
        elif self.gross_salary >= 90000 and self.gross_salary <= 99999:
            self.nhif_deductions = 1600
        elif self.gross_salary >= 100000:
            self.nhif_deductions = 1700
        # return self.nhif_deductions



    def paye(self):
        # payee1= 0
        # payee2= 0
        # payee3= 0
        # payee4= 0
        # payee5 = 0

        # if self.taxable_income > 0 and self.taxable_income <=12298:
        #     payee1 = 10/100*self.taxable_income
        #     self.payee = payee1
        # if self.taxable_income >= 12299 and self.taxable_income <=23885:
        #     payee2 = 15/100*self.taxable_income
        #     # print("Payee 2 is: ",payee2)
        #     self.payee = payee1 + payee2
        #
        # if self.taxable_income >=23886 and self.taxable_income <=35472:
        #     payee3 = 20/100*self.taxable_income
        #     self.payee = payee1 + payee2 + payee3
        # if self.taxable_income >=35473 and self.taxable_income <=47059:
        #     payee4 = 25/100*self.taxable_income
        #     self.payee = payee1 + payee2 + payee3 + payee4
        # if self.taxable_income >= 47059:
        #     payee5 = 30/100*self.taxable_income
        #     self.payee = payee1 + payee2 + payee3 + payee4 + payee5

        if self.taxable_income <= 12298:
            self.payee = (self.taxable_income * 0.1)-self.personal_relief
        elif self.taxable_income <= 23885:
            self.payee = ((12298 * 0.1) + ((self.taxable_income - 12298) * 0.15))-self.personal_relief
        elif self.taxable_income <= 35472:
            self.payee = ((12298 * 0.1) + ((23885-12298) * 0.15)+ ((self.taxable_income - 23885) * 0.20))-self.personal_relief
        elif self.taxable_income <= 47059:
            self.payee = ((12298 * 0.1) + ((23885-12298) * 0.15)+ ((35472-23885) * 0.2)+((self.taxable_income - 35472) * 0.25))-self.personal_relief
        else:
            self.payee = ((12298 * 0.1) + ((23885-12298) * 0.15) + ((35472-23885) * 0.2) + ((47059-35472) * 0.25)+((self.taxable_income - 47059) * 0.3))-self.personal_relief



        # return self.payee
    def totalDeductions(self):
        self.total_deductions = self.payee + self.nhif_deductions+self.nssf_deductions+self.pension+self.other_deductions

    def netSalary(self):
        self.net_salary = self.gross_salary-self.total_deductions
        # print(self.net_salary)# return self.net_salary




