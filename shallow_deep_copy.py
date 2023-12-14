import copy

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


class Company:
    def __init__(self, boss, employee) -> None:
        self.boss = boss
        self.employee = employee

p1 = Person("Alex", 25)
p2 = Person("Ajay", 27)

# Shallow Copying
p2 = copy.copy(p1)
p2.age = 28
print(p1.age)
print(p2.age)

# Deep Copying
company = Company(p1, p2)
company_clone = copy.deepcopy(company)
new_age = company_clone.boss.age = 50
print(new_age)
print(company.boss.age)