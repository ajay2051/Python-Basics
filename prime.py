# def is_prime(num):
#     if num == 2:
#         return True
    
#     if num % 2 == 0:
#         return False

#     for i in range(3, num):
#         if num % i == 0:
#             return False
#         return True

# prime_list = [n for n in range(2, 100) if is_prime(n)]
# print(prime_list)


def is_prime(num):
    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for i in range(3, num):
        if num % i == 0:
            return False
        return True

a = [n for n in range(2, 100) if is_prime(n)]
print(a)