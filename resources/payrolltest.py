from tkinter import messagebox

from payroll import Payroll
from tkinter import*
app = Tk()
app.title("KRA Calc")
app.geometry("500x500")
app.wm_iconbitmap('tax1.ico')



def printDetails(emp_name,KRA_PIN,id_number,basic_salary,allowances,other_deductions):
    # basic_salary = int(basic_salary)
    empl1= Payroll(emp_name,KRA_PIN,id_number,int(basic_salary),int(allowances),int(other_deductions))
    # empl2 = Payroll("Aaron Mwanzia", "A0123456789W", 29094964, 220000, 0, 0)
    # print("Name is: ", empl1.emp_name)
    # print("KRA PIN is: ", empl1.KRA_PIN)
    # print("ID number is: ", empl1.id_number)
    # print("Basic salary: ", empl1.basic_salary)
    # print("Allowances: ", empl1.allowances)
    # print("Other deductions: ", empl1.other_deductions)
    # # print("Pension: ", empl1.pension)
    # print("Gross Salary: ", empl1.gross_salary)
    # print("NSSF Deductions: ", empl1.nssf_deductions)
    # print("Taxable Income: 	{:.2f}".format(empl1.taxable_income))
    # print("NHIF Deductions: ", empl1.nhif_deductions)
    # print("PAYE: {:.2f}".format(empl1.payee))
    # print("Total deductions: {:.2f}".format(empl1.total_deductions))
    # print("Net Salary: {:.2f}".format(empl1.net_salary))

    return "Name: " + empl1.emp_name + "\n" \
           + "Basic salary: {:.2f}".format(empl1.basic_salary)+ "\n" \
           + "KRA PIN is: " + str(empl1.KRA_PIN) + "\n" \
           + "ID number is: " + str(empl1.id_number) + "\n" \
           + "Basic salary: {:.2f}".format(empl1.basic_salary) + "\n" \
           + "Allowances: {:.2f}".format(empl1.allowances) + "\n" \
           + "Other deductions: {:.2f}".format(empl1.other_deductions) + "\n" \
           + "Pension: {:.2f}".format(empl1.pension) + "\n" \
           + "Gross Salary: {:.2f}".format(empl1.gross_salary) + "\n" \
           + "NSSF Deductions: {:.2f}".format(empl1.nssf_deductions) + "\n" \
           + "Taxable Income: {:.2f}".format(empl1.taxable_income)+ "\n" \
           + "NHIF Deductions: {:.2f}".format(empl1.nhif_deductions) + "\n" \
           + "PAYE: {:.2f}".format(empl1.payee) + "\n" \
           + "Total deductions: {:.2f}".format(empl1.total_deductions)+"\n"\
           +"Net Salary: {:.2f}".format(empl1.net_salary)




# messagebox.showinfo("These are the details: ", printDetails())



label1 = Label(app, text="Employee Name:")
label2 = Label(app, text="KRA Pin:")
label3 = Label(app, text="ID No:")
label4 = Label(app, text="Basic Salary")
label5 = Label(app, text="Allowances")
label6 = Label(app, text="Other Deductions")

entry1 = Entry(app)
entry2 = Entry(app)
entry3 = Entry(app)
entry4 = Entry(app)
entry5 = Entry(app)
entry6 = Entry(app)

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=2, column=0)
label4.grid(row=3, column=0)
label5.grid(row=4, column=0)
label6.grid(row=5, column=0)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
entry3.grid(row=2,column=1)
entry4.grid(row=3,column=1)
entry5.grid(row=4,column=1)
entry6.grid(row=5,column=1)


#
# frame = Frame(app,width=300, height=200)
# frame.bind("<button1>",button1.bind(printDetails))

def showDetails():
    details = printDetails(entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get())
    text_field = Text(master=app,height=20, width=30)
    text_field.grid(row=7,column=1)

    text_field.insert(END,details)

button1 = Button(app, text="Calculate", command=showDetails)
button1.grid(row=6,column=1)


app.mainloop()