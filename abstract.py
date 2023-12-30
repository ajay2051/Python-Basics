from abc import ABC, abstractmethod


class Shape(ABC):
    """Object cannot be created from Abstract Class"""

    @abstractmethod
    def print_area(self):  # Abstract Function does not return anything.
        pass


class Rectangle(Shape):
    def __init__(self):
        self.length = 3
        self.breadth = 4

    def print_area(self):  # It is compulsory to define print_area method because it is defined in Abstract Base Class
        return self.length * self.breadth


r1 = Rectangle()
print(r1.print_area())
