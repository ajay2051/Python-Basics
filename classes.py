# class Employee:
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@gmail.com'


# emp1 = Employee('Ajay', 'Thakur', 5000)
# print(emp1.first)
# print(emp1.email)

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        # print(self.first + self.last)


emp_1 = Employee('ajay', 'thakur', 5000)
emp_2 = Employee('Panche', 'Chaudhary', 1000)
# emp1.fullname()
print(emp_2.fullname())
