def cube(numbers):
    for i in numbers:
        yield i * i * i

results =   cube([1,2,3])
for result in results:
    print(result)