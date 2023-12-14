class Parent:
    def __init__(self, name) -> None:
        self.name = name

    def get_name(self):
        return self.name


class Child(Parent):
    def __init__(self, name, age) -> None:
        super().__init__(name)
        self.age = age

    def get_age(self):
        return self.age


class GrandChild(Child):
    def __init__(self, name, age, location) -> None:
        super().__init__(name, age)
        self.location = location

    def get_location(self):
        return self.location


a = GrandChild("Ajay", 25, "Ktm")
print(a.get_name())
print(a.get_age())
print(a.get_location())
