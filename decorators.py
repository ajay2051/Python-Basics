# def outer_function(msg):
#     def inner_function():
#         print(msg)
#     return inner_function

# a = outer_function('ajay')
# b = outer_function('abhay')
# a()
# b()


def decorator_function(original_function):
    def wrapper_function():
        print('Executing...!')
        original_function()
        print('Executed...!')

    return wrapper_function


@decorator_function
def display_function():
    print('I love Nepal')


display_function()


# Python Decorator allows to change the behavior of a function without modifying the function itself and takes another function as parameter.
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('Start....!')
        original_function(*args, **kwargs)
        print('Finish...!')

    return wrapper_function


@decorator_function
def first_function():
    print('Hello')


@decorator_function
def second_function(name, address):
    print(f'He is {name}. lives in {address}')


first_function()
second_function('Ajay', 'ktm')


def first_function(parameter):
    def second_function(*args, **kwargs):
        print('Executing...')
        parameter(*args, **kwargs)
        print('Executed.......')

    return second_function


@first_function
def display(name):
    print(name)


display('Ajay')


def decorator_function(original_function):
    """This is the decorator function which decorates other functions"""

    def wrapper_function(*args, **kwargs):
        print("Start.....")
        result = original_function(*args, **kwargs)
        print(result)
        print("End......")
        print("Start Again........")
        result = original_function(*args, **kwargs)
        print(result)
        print("Ended...........")
        return result  # Return the result obtained from the original function

    return wrapper_function


@decorator_function
def add_num(a, b):
    """This function add two numbers"""
    return a + b


results = add_num(2, 3)
print(f"The sum is {results}")

