some_list = ["1", "2", "5"]
print(some_list.pop(2))


# Index and Pop Problems
def f1(x):
    for i in x:
        x.pop()
        print(x)
        print(i, end="")


a = [0, 1, 2, 3, 4, 5, 6]
f1(a)
