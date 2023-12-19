# def square(x):
#     return x * x

# def cube(x):
#     return x * x * x

# # f = square(4)
# f = square
# print(f(6))
# print(square)

# def my_map(func, arg_list):
#     result = []
#     for i in arg_list:
#         result.append(func(i))
#     return result

# squares = my_map(square, [1,2,3])
# print(squares)

def html_tag(tag):
    def wrap_text(msg):
        print('<{0}><{1}></{0}>'.format(tag, msg))

    return wrap_text


print_h1 = html_tag('h1')
print_h1('Test Headline')
print_h1('Hello World')

print_p = html_tag('p')
print_p('Test Paragraph')
print_p('Another Paragraph')
