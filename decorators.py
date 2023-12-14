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


# Python Decorator allows to change the the behavior of a function without modifying the function itself and takes another function as parameter.
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


