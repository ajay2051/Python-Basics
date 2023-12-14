class Car:
    def start(self):
        print("Start The Car")


class Flyable:
    def start(self):
        print("Start the Flyable Car")


class FlyingCar(Car, Flyable):
    def start(self):
        return super().start()


if __name__ == "__main__":
    c = FlyingCar()
    c.start()
