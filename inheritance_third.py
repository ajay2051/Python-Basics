class Employee:
    raise_amount = 1.10

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount

class Developers(Employee):
    def __init__(self, first, last, pay, lang):
        super().__init__(first, last, pay)
        self.lang = lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

        def add_emp(self, emp):
            if self.emp not in employees:
                self.employees.append(self.emp)

        def rem_emp(self, emp):
            if self.emp in employees:
                self.employees.remove(self.emp)

     



