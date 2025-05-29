# Pass by Value

# When we pass an argument to a function, it is stored locally (in the stack memory), i.e., the scope of these variables lies with in
# the function and these will not have effect the values of the global variables (variables outside function).
#
# In Python, "passing by value" is possible only with the immutable types such as integers, floats, strings, and tuples. Even though we pass
# these as a reference, the object itself cannot be changed.

n=1
def modify_number(n):
    print(f"Before: {n}")
    n += 1
    print(f"After: {n}")
modify_number(n)
print(n)


# Pass by reference

# Unlike in "Call by Value", When we call a method by "passing the reference of a value (object)", the original value will be modified
#
# The formal and actual arguments are in the same address space, Since we are passing the reference address of the arguments, if we modify a local variable, it is reflected throughout the function.
#
# In Python, we can only pass the reference of mutable types such as lists, dictionaries, and sets, to a function.


my_list = [1, 2, 3]
def modify_list(my_list):
    print(f"Before: {my_list}")
    my_list.append(4)
    print(f"After: {my_list}")
modify_list(my_list)
print(my_list)