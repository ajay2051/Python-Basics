# def square_numbers(nums):
#     for i in nums:
#         yield i * i


# my_nums =  square_numbers([1,2])
# for num in my_nums:
#     print(num)

# A generator is a function that returns an object(iterator) which we can iterate over.
# Generators are useful when we want to produce a large sequence of values,
# but we don't want to store all of them in memory at once.


def fib(n):
    p, q = 0, 1
    while p < n:
        yield p
        p, q = q, p + q


fib(10)
for i in fib(10):
    print(i)


def fib(n):
    p, q = 0, 1
    sum = 0
    while p < n:
        yield p
        sum += p
        p, q = q, p + q
    yield sum

n = 23
fib_seq = fib(n)
print("Fibonacci numbers up to", n, "are:")
for i in fib_seq:
    print(i, end=" ")
