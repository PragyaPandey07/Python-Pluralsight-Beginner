from employee_class import Employee 
from employee_inheritance import SalariedEmployee, HourlyEmployee, CommissionEmployee

class Company :
    def __init__(self) :
        self.employees = []
    
    def add_employee(self, new_employee) :
        self.employees.append(new_employee)

    def show_employees(self):
        print("The Employees are:")
        for employee in self.employees :
            print(employee.fname, employee.lname)
        print('----------END--------------')

    def show_salary(self):
        for employee in self.employees :
            print(f'{employee.fname} {employee.lname} : {employee.calculate_pay():,.2f}')
            print('----------------------------') 

def main():
    my_company = Company()

    employee1 = Employee('Pragya', 'Pandey', '25000')
    my_company.add_employee(employee1)
    employee2 = Employee('Pranav', 'Pandey', '20000')
    my_company.add_employee(employee2)
    employee3 = Employee('Rajendra', 'Bhat', '50000')
    my_company.add_employee(employee3)

    my_company.show_employees()
    my_company.show_salary()

    employee_a = SalariedEmployee('Pragya', 'Pandey', '150000')
    my_company.add_employee(employee_a)
    employee_b = HourlyEmployee('Pranav', 'Pandey', 45, 20)
    my_company.add_employee(employee_b)
    employee_c = CommissionEmployee('Nidhi', 'Tiwari', '30000', 15, 20)
    my_company.add_employee(employee_c)

    my_company.show_employees()
    my_company.show_salary()

main()
        