class Employee:
    raise_amount = 1.04

    def __init__(self,first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format (self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developers(Employee):
    raise_amount = 1.05

    def __init__(self, first, last, pay, lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self,first, last,pay)
        self.lang = lang

dev_1 = Developers('Ajay', 'Thakur', 20000, 'Python')
print(dev_1.lang)
print(dev_1.fullname())
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

