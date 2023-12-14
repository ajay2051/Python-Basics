a = lambda x, y: x * y
print(a(2, 7))


numbers = [1, 2, 3, 4, 5]
multipliers = [lambda x: i * x for i in numbers]
result = [m(2) for m in multipliers]
print(result)
