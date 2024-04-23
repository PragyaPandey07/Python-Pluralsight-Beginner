class Employee :
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def calculate_pay(self) :
        return float(self.salary)/12 