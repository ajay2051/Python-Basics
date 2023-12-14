# Method Overloading allows multiple methods in the same class to have the same name but different parameters.


class OverloadingExample:
    def add(self, a, b):
        print(a + b)

    def add(self, a, b, c):
        print(a + b + c)


a = OverloadingExample()
a.add(1, 2, 3)

# Python doesnot support method overloading.
