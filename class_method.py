#  Class methods have access to the class itself and can access class-level variables, methods, and attributes.


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @classmethod
    def emp(cls, emp_str):
        first, last, pay = emp_str.split("_")
        return cls(first, last, pay)


emp_str_1 = "ajay_thakur_25000"
a = Employee.emp(emp_str_1)
print(a.first)
