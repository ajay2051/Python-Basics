# Impelementing our own generator


my_lst = [1, 5, 7, 8, 9, 6, 3, 5, 4, 8, 2, 4]


def chunk(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


a = chunk(my_lst, 3)
print(list(a))


# Generator Comprehension
n = 3
a = (my_lst[i : i + n] for i in range(0, len(my_lst), n))
print(list(a))

# List Comprehension
b = [my_lst[i : i + n] for i in range(0, len(my_lst), n)]
print(b)
