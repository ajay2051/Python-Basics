def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
print(factorial(4))
print(factorial(3))


def fb(n):
    if n == 1 or n == 0:
        return n
    else:
        return fb(n - 1) + fb(n - 2)

t = 10
if t <= 0:
    print("Enter positive number")
else:
    for i in range(t):
        print(fb(i))
