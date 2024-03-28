# A closure is a function whose returns value depends on the value of one or more variables which are declared outside the function.


def outer_function(text):
    def wrapper_function():
        print(text)

    return wrapper_function


a = outer_function("Ajay")
del outer_function
a()

# import logging

# def logger(func):

#     def log_func(*args):
#         logging.info('Running with "{}" arguments {} '.format(func.__name__, args))
#         print(func(*args))
#     return log_func

# def add(x, y):
#     return x + y


# def sub(x, y):
#     return x - y

# add_logger = logger(add)
# sub_logger = logger(sub)

# add_logger(2, 3)
# sub_logger(6, 7)
