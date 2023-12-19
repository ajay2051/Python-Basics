class Vehicle:
    @staticmethod
    def info(self):
        print("Vehicle Info")


class Car(Vehicle):
    @staticmethod
    def car_info(self):
        print("Car Info")


class Truck(Car):
    @staticmethod
    def truck_info(self):
        print("Truck Info")
