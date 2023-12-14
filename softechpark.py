# list1 = [3,4,5,2,1,0]
# print(list1.pop(1))

# a = 'Hello World'
# print(a[::-1])

# func = lambda a, b : (a ** b)
# print(func(float(10),20))

# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

# first_name = "XYZ"
# person = Person(first_name, "ABC")
# person.first_name = "LMN"
# person.last_name = "PQR"
# print(person.first_name, person.last_name)


# list1 = ['s', 'r', 'a', 's']
# list2 = ['a', 'a', 'n', 'h'],
# r = ["".join([i, j]) for i, j in zip(list1, list2)]
# print(list(r))

count = 0
my_string = 'HELLO WORLD'
my_char = 'O'

for i in my_string:
    if i == my_char:
        count += 1

print(count)
