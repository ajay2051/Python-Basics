# Method overriding allows a parent class and a child class to have methods with same name and same parameters.


class Overriding1:
    def display(self):
        print("hello")


class Overriding2:
    def display(self):
        print("hello world")


o1 = Overriding1()
o1.display()

o2 = Overriding2()
o2.display()
