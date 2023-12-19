class Employee:
    num_of_employee = 0
    raise_amount = 1.4

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_employee += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def address(self, place):
        return "{} {}".format(self.first, place)


emp_1 = Employee('ajay', 'thakur', 10000)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(emp_1.address("Npj"))
