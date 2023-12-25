# my_nums = list(x * x for x in [1, 2 ,3])
# print(my_nums)

# comprehension = [expression for variable in iterable]

# Lambda functions are similar to user-defined functions but without a name.
# They're commonly referred to as anonymous functions.


nums = [1, 2, 3, 4, 5, 6]
my_nums = [n for n in nums if n % 2 == 0]
print(my_nums)

my_list = filter(lambda n: n % 2 == 0, nums)
print(list(my_list))

square = map(lambda n: n * n, nums)
print(list(square))

result = [None if i % 2 == 0 else i for i in range(2, 9)]
print(result)

# Conditionals in List Comprehension
number_list = [x for x in range(20) if x % 2 == 0]
print(number_list)

# Nested IF with List Comprehension
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)

# if...else With List Comprehension
obj = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
print(obj)

# Transpose of a Matrix using List Comprehension
matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print(transpose)
