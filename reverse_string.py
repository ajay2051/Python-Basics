name = "hello kathmandu"
splitted_name = name.split()
for i in splitted_name:
    a = i[::-1]
    for r in a:
        print("".join(r), end="")
