# class Employee:

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay


#     @property
#     def email(self):
#         return '{}{}@gmail.com'.format(self.first, self.last)

#     @property
#     def fullname(self):
#         return '{} {}'.format (self.first, self.last)

#     @fullname.setter
#     def fullname(self, name):
#         first, last = name.split(' ')
#         self.first = first
#         self.last = last

#     @fullname.deleter
#     def fullname(self):
#         print('Delete Done!')
#         self.first = None
#         self.last = None


# emp_1 = Employee('Ajay', 'Thakur', 10000)
# #emp_1.first = "Bijay"
# emp_1.fullname = 'Bijay Singh'
# print(emp_1.fullname)
# print(emp_1.email)
# del emp_1.fullname


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return "{} {} @email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last


emp_1 = Employee("Ajay", "Thakur")
emp_1.fullname = "Bijay Singh"
print(emp_1.email)
print(emp_1.fullname)


class Student:
    def __init__(self, name) -> None:
        self.__name = name

    @property
    def student_name(self):
        return self.__name

    @student_name.setter
    def student_name(self, name):
        self.__name = name

    @student_name.deleter
    def student_name(self):
        del self.__name

std = Student("Ajay")
print(std.student_name)
std.student_name = "Hello"
print(std.student_name)
del std.student_name
print(std.student_name)
