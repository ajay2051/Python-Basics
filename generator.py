# def square_numbers(nums):
#     for i in nums:
#         yield i * i


# my_nums =  square_numbers([1,2])
# for num in my_nums:
#     print(num)

# A generator is a function that returns an object(iterator) which we can iterate over.


def fib(n):
    p, q = 0, 1
    while p < n:
        yield p
        p, q = q, p + q


fib(10)
for i in fib(10):
    print(i)
