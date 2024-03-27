class First:
    def start(self):
        print("Car Started")


class Second:
    def start(self):
        print("Car is already started")


class Third(First, Second):
    def third(self):
        super().start()


a = Third()
a.third()
