def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ("Math", "Science")
details = {"name": "ajay", "age": "27"}
student_info(*courses, **details)


def std_list(*args, **kwargs):
    for item in args:
        print(item)

    for key, value in kwargs.items():
        print(f"{key} is a {value}")


a = ("ajay", "mohan")
b = {"ajay": "programmer", "bijay": "driver"}
std_list(*a, **b)