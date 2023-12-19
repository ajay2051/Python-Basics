# Solution to multiply string and integer
def solution(s, i):
    numbers = {"one": 1, "two": 2}
    if s in numbers:
        return int(numbers[s] * i)
    else:
        return ""


a = solution("two", 2)
print(a)


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
