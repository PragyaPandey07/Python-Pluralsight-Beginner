class Employee :
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class SalariedEmployee(Employee) :
    def __init__(self, fname, lname, package):
        super().__init__(fname, lname)
        self.package = package

    def calculate_pay(self) :
        return float(self.package)/12

class HourlyEmployee(Employee) :
    def __init__(self, fname, lname, weekly_hours, hourly_rate):
        super().__init__(fname, lname)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate

    def calculate_pay(self) :
        return self.weekly_hours * self.hourly_rate

class CommissionEmployee(SalariedEmployee) :
    def __init__(self, fname, lname, package, sales_num, comm_rate):
        super().__init__(fname, lname, package)
        self.sales_num = sales_num
        self.comm_rate = comm_rate

    def calculate_pay(self):
        regular_salary = super().calculate_pay() 
        commission = self.sales_num * self.comm_rate
        return regular_salary + commission
    
# def main():
    # employee1 = SalariedEmployee('Pragya', 'Pandey', '150000')
    # print(employee1.calculate_pay())
    # employee2 = HourlyEmployee('Pranav', 'Pandey', 45, 20)
    # print(employee2.calculate_pay())
    # employee3 = CommissionEmployee('Nidhi', 'Tiwari', '30000', 15, 20)
    # print(employee3.calculate_pay())

# main()