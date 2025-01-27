# Note: All string methods returns new values. They do not change the original string.

course = 'Python for beginners'
print(course[-2:])
print(course[0:])
print(course[1:5])
print(course[5:])
print(course[:2])
print(course[2:-2])
print(course.find('beginners'))
print(course.strip())
course1 = course.split()
print(course1)
course2 = ''.join(course1)
print(course2)

