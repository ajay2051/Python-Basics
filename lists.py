name = ["Ajay", "Abhay", "Shyam", "Mohan"]
# print(name[0])
# print(name[-2])
# print(name[2:])
# print(name[1:5])

num = [2, 4, 3, 6, 7, 9]
num.append(2)
num.insert(2, 15)
print(num)


fruits = ["banana", "cherry", "apple"]
copied_fruits = fruits.copy()
copied_fruits.append("lemon")
print(copied_fruits)


# largest number in list

# numbers = [2,5,4,6,10,7,6]
# largest = numbers[0]
# for number in numbers:
#     if number > largest:
#         largest = number
# print(largest)


a = [1, 2, 3]
b = ["a", "b", "c"]
for val1, val2 in zip(b, a):
    print(val1, val2)
